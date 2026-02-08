"""
Add/Update Expense tab: select date, load existing expenses, edit in form, submit.
Logic unchanged; only UI, layout, and feedback improved.
"""

import streamlit as st
from datetime import datetime
from api_client import fetch_expenses_for_date_uncached, post_expenses_for_date
from ui_components import section_header, inject_custom_css

CATEGORIES = ["Rent", "Food", "Shopping", "Entertainment", "Other"]


def add_update_tab():
    inject_custom_css()
    section_header(
        "Add or update expenses",
        "Choose a date and enter or edit expenses. Leave amount 0 to skip a row.",
    )

    selected_date = st.date_input(
        "Date",
        value=datetime(2024, 8, 1).date(),
        help="Expenses will be saved for this date. Existing entries for this date will be replaced on submit.",
        label_visibility="visible",
    )

    with st.spinner("Loading expenses for this date…"):
        existing_expenses = fetch_expenses_for_date_uncached(selected_date)

    with st.form(key="expense_form"):
        st.markdown("**Expense entries**")
        st.caption("Use the first 5 rows. Set amount to 0 to omit an entry.")

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i].get("notes") or ""
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=float(amount),
                    key=f"amount_{i}",
                    label_visibility="collapsed",
                    help="Enter 0 to skip this row.",
                )
            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=CATEGORIES,
                    index=CATEGORIES.index(category) if category in CATEGORIES else 0,
                    key=f"category_{i}",
                    label_visibility="collapsed",
                    help="Spending category.",
                )
            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"notes_{i}",
                    label_visibility="collapsed",
                    placeholder="Optional notes…",
                    help="Short description or note.",
                )

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input,
            })

        submit_button = st.form_submit_button("Save expenses")

    if submit_button:
        filtered = [e for e in expenses if e["amount"] > 0]
        if not filtered:
            st.warning("No expenses to save. Add at least one entry with amount > 0.")
            return
        success, err = post_expenses_for_date(selected_date, filtered)
        if success:
            st.success("Expenses updated successfully!")
        else:
            st.error(err or "Failed to update expenses.")
