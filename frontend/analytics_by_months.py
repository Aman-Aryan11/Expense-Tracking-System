"""
Analytics by months: monthly summary bar chart and table.
Logic unchanged; uses api_client and ui_components.
"""

import streamlit as st
import pandas as pd
from api_client import fetch_monthly_summary
from ui_components import (
    section_header,
    chart_card,
    chart_card_start,
    chart_card_end,
    empty_state,
    inject_custom_css,
)


def analytics_months_tab():
    inject_custom_css()
    section_header(
        "Expense breakdown by month",
        "Total spending per month across all categories.",
    )

    with st.spinner("Loading monthly summary…"):
        monthly_summary = fetch_monthly_summary()

    if monthly_summary is None:
        st.error("Could not load monthly summary. Is the backend running?")
        return

    if not monthly_summary:
        empty_state(
            "No monthly data yet.",
            "Add expenses to see the breakdown by month.",
        )
        return

    df = pd.DataFrame(monthly_summary)
    df = df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total_amount": "Total",
    })
    df_sorted = df.sort_values(by="Month Number", ascending=False).set_index("Month Number")

    chart_card("Monthly totals", "Total spending per month.")
    chart_card_start()
    st.bar_chart(
        data=df_sorted.set_index("Month Name")["Total"],
        use_container_width=True,
        height=400,
    )
    chart_card_end()

    df_display = df_sorted.copy()
    df_display["Total"] = df_display["Total"].map("{:.2f}".format)
    st.dataframe(df_display.sort_index(), use_container_width=True, hide_index=True)
