from backend import db_helper

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date('2024-08-15')

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10
    assert expenses[0]['category'] == 'Shopping'
    assert expenses[0]['notes'] == 'Bought potatoes'

def test_insert_and_delete_expense():
    db_helper.insert_expense('2024-12-01', 25.0, 'Transport', 'Bus fare')
    expenses = db_helper.fetch_expenses_for_date('2024-12-01')
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 25.0
    assert expenses[0]['category'] == 'Transport'
    assert expenses[0]['notes'] == 'Bus fare'

    db_helper.delete_expenses_for_date('2024-12-01')
    expenses_after_deletion = db_helper.fetch_expenses_for_date('2024-12-01')
    assert len(expenses_after_deletion) == 0

def test_fetch_expense_summary():
    summary = db_helper.fetch_expense_summary('2024-08-01', '2024-08-05')
    summary_dict = {record['category']: record['total_amount'] for record in summary}

    assert summary_dict.get('Shopping') == 670
    assert summary_dict.get('Food') == 1225
    assert summary_dict.get('Other') == 90

def test_empty_expense_summary():
    summary = db_helper.fetch_expense_summary('2023-01-01', '2023-01-31')
    assert summary == []

def test_fetch_expenses_for_invalid_date():
    expenses = db_helper.fetch_expenses_for_date('2024-02-30')
    assert len(expenses) == 0

def test_delete_expenses_for_nonexistent_date():
    db_helper.delete_expenses_for_date('2025-01-01')  
    expenses = db_helper.fetch_expenses_for_date('2025-01-01')
    assert expenses == []