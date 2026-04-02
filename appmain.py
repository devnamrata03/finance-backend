from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, Base, SessionLocal
from app.models import Transaction

app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home
@app.get("/")
def home():
    return {"message": "Finance API Running 🚀"}


# ➕ Add Transaction
@app.post("/add")
def add_transaction(amount: float, type: str, category: str, date: str, notes: str, db: Session = Depends(get_db)):

    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    if type not in ["income", "expense"]:
        raise HTTPException(status_code=400, detail="Type must be income or expense")

    new_data = Transaction(
        amount=amount,
        type=type,
        category=category,
        date=date,
        notes=notes
    )

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data


# 📄 Get All Transactions
@app.get("/transactions")
def get_all(db: Session = Depends(get_db)):
    return db.query(Transaction).all()


# ❌ Delete
@app.delete("/delete/{id}")
def delete_transaction(id: int, db: Session = Depends(get_db)):

    record = db.query(Transaction).filter(Transaction.id == id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()

    return {"message": "Deleted successfully"}


# ✏️ Update
@app.put("/update/{id}")
def update_transaction(id: int, amount: float, type: str, category: str, date: str, notes: str, db: Session = Depends(get_db)):

    record = db.query(Transaction).filter(Transaction.id == id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    record.amount = amount
    record.type = type
    record.category = category
    record.date = date
    record.notes = notes

    db.commit()

    return {"message": "Updated successfully"}


# 🔍 Filter
@app.get("/filter")
def filter_data(type: str = None, category: str = None, db: Session = Depends(get_db)):

    query = db.query(Transaction)

    if type:
        query = query.filter(Transaction.type == type)

    if category:
        query = query.filter(Transaction.category == category)

    return query.all()


# 📊 Summary
@app.get("/summary")
def get_summary(db: Session = Depends(get_db)):

    data = db.query(Transaction).all()

    total_income = sum(x.amount for x in data if x.type == "income")
    total_expense = sum(x.amount for x in data if x.type == "expense")

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }
