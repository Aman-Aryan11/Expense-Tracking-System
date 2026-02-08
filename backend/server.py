from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import db_helper
from datetime import date

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    """Get expenses for a specific date."""
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=404, detail="Expenses not found")
    return expenses

@app.post("expenses/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses: List[Expense]):
    """Add or update expenses for a specific date."""
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(
            expense_date,
            expense.amount,
            expense.category,
            expense.notes
        )
    return {"message": "Expenses updated successfully"}

@app.post("/analytics")
def get_analytics(date_range: DateRange):
    """Get expense analytics for a date range."""
    data = db_helper.fetch_expense_summary(
        date_range.start_date,
        date_range.end_date
    )
    if data is None:
        raise HTTPException(status_code = 404, detail = "No analytics data found")
    
    total_expense = sum(item['total_amount'] for item in data)

    breakdown = {}
    for item in data:
        percentage = (item['total_amount'] / total_expense) * 100 if total_expense != 0 else 0
        breakdown[item['category']] = {
            "total_amount": item['total_amount'],
            "percentage": percentage
        }
    return breakdown

@app.get("/monthly_summary/")
def get_analytics():
    monthly_summary = db_helper.fetch_monthly_expense_summary()
    if monthly_summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve monthly expense summary from the database.")

    return monthly_summary