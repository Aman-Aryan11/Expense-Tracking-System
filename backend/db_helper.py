import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit=False):
    """Context manager for MySQL database cursor."""
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'expense_manager'
    )

    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()

def fetch_expenses_for_date(expense_date):
    """Fetch expense for a specific date."""
    with get_db_cursor() as cursor:
        query = "SELECT * FROM expenses WHERE expense_date = %s"
        cursor.execute(query, (expense_date,))
        return cursor.fetchall()
    
def delete_expenses_for_date(expense_date):
    """Delete expenses for a specific date."""
    with get_db_cursor(commit=True) as cursor:
        query = "DELETE FROM expenses WHERE expense_date = %s"
        cursor.execute(query, (expense_date,))

def insert_expense(expense_date, amount, category, notes):
    """Insert a new expense record."""
    with get_db_cursor(commit=True) as cursor:
        query = """
        INSERT INTO expenses (expense_date, amount, category, notes)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (expense_date, amount, category, notes))

def fetch_expense_summary(start_date, end_date):
    """Fetch expense summary between two dates."""
    with get_db_cursor() as cursor:
        query = """
        SELECT category, SUM(amount) AS total_amount
        FROM expenses
        WHERE expense_date BETWEEN %s AND %s
        GROUP BY category
        """
        cursor.execute(query, (start_date, end_date))
        return cursor.fetchall()

if __name__ == "__main__":
    # expenses = fetch_expenses_for_date('2024-09-30')
    # print(expenses)

    # insert_expense('2024-11-08', 50.0, 'Food', 'Lunch at cafe')
    # delete_expenses_for_date('2024-11-08')

    summary = fetch_expense_summary('2024-08-01', '2024-08-05')
    for record in summary:
        print(record)