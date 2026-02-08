"""
Analytics by category: date range, then bar chart and table of category breakdown.
Logic unchanged; uses api_client and ui_components.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from api_client import fetch_analytics
from ui_components import (
    section_header,
    chart_card,
    chart_card_start,
    chart_card_end,
    empty_state,
    inject_custom_css,
)


def analytics_category_tab():
    inject_custom_css()
    section_header(
        "Expense breakdown by category",
        "Pick a date range to see spending by category (total and share).",
    )

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(
            "Start date",
            value=datetime(2024, 8, 1).date(),
            help="Start of the period to analyze.",
        )
    with col2:
        end_date = st.date_input(
            "End date",
            value=datetime(2024, 8, 5).date(),
            help="End of the period to analyze.",
        )

    if st.button("Get analytics", type="primary"):
        if start_date > end_date:
            st.error("Start date must be before or equal to end date.")
        else:
            with st.spinner("Loading analytics…"):
                response = fetch_analytics(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))

            if not response:
                empty_state(
                    "No analytics data for this range.",
                    "Add expenses in this period or try a different range.",
                )
                return

            data = {
                "Category": list(response.keys()),
                "Total": [response[c]["total_amount"] for c in response],
                "Percentage": [response[c]["percentage"] for c in response],
            }
            df = pd.DataFrame(data)
            df_sorted = df.sort_values(by="Percentage", ascending=False)

            chart_card("Category share (%)", "Percentage of total spending per category.")
            chart_card_start()
            st.bar_chart(data=df_sorted.set_index("Category")[["Percentage"]], use_container_width=True)
            chart_card_end()

            df_display = df_sorted.copy()
            df_display["Total"] = df_display["Total"].map("{:.2f}".format)
            df_display["Percentage"] = df_display["Percentage"].map("{:.2f}".format)
            st.dataframe(df_display, use_container_width=True, hide_index=True)
