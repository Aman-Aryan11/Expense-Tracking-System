"""
Cached API client for the Expense Tracking System.
Uses st.cache_data to avoid redundant re-renders and repeated backend calls.
All business logic and URLs stay here; UI only consumes returned data.
"""

import streamlit as st
import requests
from datetime import date

# Assumption: Backend runs at localhost:8000. Change if deployed elsewhere.
API_URL = "http://localhost:8000"


@st.cache_data(ttl=60)
def fetch_expenses_for_date(_date: date):
    """
    GET /expenses/{date}. Returns list of expense dicts or [] on error/404.
    Not cached for long so that after adding/updating expenses, data refreshes.
    """
    try:
        response = requests.get(f"{API_URL}/expenses/{_date}", timeout=5)
        if response.status_code == 200:
            return response.json()
        return []
    except requests.RequestException:
        return []


def fetch_expenses_for_date_uncached(date_val: date):
    """
    Same as above but bypasses cache. Use in Add Expense so after submit we see fresh data.
    """
    try:
        response = requests.get(f"{API_URL}/expenses/{date_val}", timeout=5)
        if response.status_code == 200:
            return response.json()
        return []
    except requests.RequestException:
        return []


@st.cache_data(ttl=60)
def fetch_monthly_summary():
    """
    GET /monthly_summary/. Returns list of {expense_month, month_name, total_amount}.
    """
    try:
        response = requests.get(f"{API_URL}/monthly_summary/", timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.RequestException:
        return None


@st.cache_data(ttl=60)
def fetch_analytics(start_date: str, end_date: str):
    """
    POST /analytics/ with {start_date, end_date}. Returns category breakdown.
    """
    try:
        response = requests.post(
            f"{API_URL}/analytics/",
            json={"start_date": start_date, "end_date": end_date},
            timeout=5,
        )
        if response.status_code == 200:
            return response.json()
        return None
    except requests.RequestException:
        return None


def post_expenses_for_date(date_val: date, expenses: list):
    """
    POST /expenses/{date} with list of {amount, category, notes}. Returns (success, error_message).
    """
    try:
        response = requests.post(
            f"{API_URL}/expenses/{date_val}",
            json=expenses,
            timeout=5,
        )
        if response.status_code == 200:
            return True, None
        return False, "Failed to update expenses."
    except requests.RequestException as e:
        return False, str(e)
