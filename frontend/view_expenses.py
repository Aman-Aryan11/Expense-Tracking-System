"""
View Expenses tab: pick a date and see expenses for that day in a table.
Read-only; no business logic changes.
"""

import streamlit as st
from datetime import datetime
from api_client import fetch_expenses_for_date_uncached
from ui_components import section_header, empty_state, inject_custom_css


def view_expenses_tab():
    inject_custom_css()
    section_header("View expenses", "Select a date to see all expenses for that day.")

    selected_date = st.date_input(
        "Select date",
        value=datetime(2024, 8, 1).date(),
        help="Choose the day whose expenses you want to view.",
        label_visibility="visible",
    )

    with st.spinner("Loading…"):
        expenses = fetch_expenses_for_date_uncached(selected_date)

    if not expenses:
        empty_state(
            "No expenses for this date.",
            "Add expenses using the Add Expense tab, or pick another date.",
        )
        return

    # Build display table: Category, Amount, Notes
    rows = []
    total = 0.0
    for e in expenses:
        amount = float(e.get("amount", 0))
        total += amount
        rows.append(
            {
                "Category": e.get("category", ""),
                "Amount": f"{amount:.2f}",
                "Notes": e.get("notes", "") or "—",
            }
        )

    st.dataframe(
        rows,
        use_container_width=True,
        hide_index=True,
    )
    st.caption(f"Total for {selected_date}: **${total:,.2f}**")
