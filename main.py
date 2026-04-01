from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, SessionLocal, Base


# Database tables create karega
Base.metadata.create_all(bind=engine)

# FastAPI app start
app = FastAPI()


# Database connection function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# USER CREATE API
# -----------------------------
@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    new_user = models.User(
        name=user.name,
        email=user.email,
        role=user.role,
        status=user.status
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# -----------------------------
# CREATE FINANCIAL RECORD
# -----------------------------
@app.post("/records")
def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db)):

    new_record = models.Record(
        amount=record.amount,
        type=record.type,
        category=record.category,
        date=record.date,
        notes=record.notes
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record


# -----------------------------
# GET ALL RECORDS
# -----------------------------
@app.get("/records")
def get_records(db: Session = Depends(get_db)):

    records = db.query(models.Record).all()

    return records


# -----------------------------
# DASHBOARD SUMMARY API
# -----------------------------
@app.get("/dashboard")
def dashboard_summary(db: Session = Depends(get_db)):

    records = db.query(models.Record).all()

    income = sum(r.amount for r in records if r.type == "income")
    expense = sum(r.amount for r in records if r.type == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }