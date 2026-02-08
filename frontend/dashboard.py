"""
Dashboard tab: key metrics, category bar chart, and monthly trend line chart.
Uses cached API calls; no change to business logic.
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from api_client import fetch_monthly_summary, fetch_analytics
from ui_components import (
    section_header,
    render_metric_card,
    chart_card,
    chart_card_start,
    chart_card_end,
    empty_state,
    inject_custom_css,
)


def dashboard_tab():
    inject_custom_css()
    section_header("Dashboard", "Overview of your spending and trends.")

    with st.spinner("Loading dashboard…"):
        monthly_summary = fetch_monthly_summary()
        if monthly_summary is None:
            st.error("Could not load monthly summary. Is the backend running?")
            return

        # Default analytics range: last 3 months or all data
        today = datetime.now().date()
        start_default = today - timedelta(days=90)
        end_default = today
        analytics = fetch_analytics(start_default.strftime("%Y-%m-%d"), end_default.strftime("%Y-%m-%d"))

    # ----- Metrics row -----
    total_expenses = sum(m.get("total_amount", 0) for m in monthly_summary)
    monthly_sorted = sorted(monthly_summary, key=lambda x: (x.get("expense_month", 0), x.get("month_name", "")))
    current_month_total = 0
    if monthly_sorted:
        # Use latest month in data as "current" for display
        latest = monthly_sorted[-1]
        current_month_total = latest.get("total_amount", 0)
        latest_month_name = latest.get("month_name", "This month")

    top_category = "—"
    if analytics:
        by_total = sorted(analytics.items(), key=lambda x: x[1].get("total_amount", 0), reverse=True)
        if by_total:
            top_category = by_total[0][0]

    col1, col2, col3 = st.columns(3)
    with col1:
        render_metric_card("Total expenses", f"${total_expenses:,.2f}")
    with col2:
        render_metric_card("Monthly (latest)", f"${current_month_total:,.2f}")
    with col3:
        render_metric_card("Highest spending category", top_category)

    st.markdown("---")

    # ----- Charts row -----
    c1, c2 = st.columns(2)

    with c1:
        chart_card("Expense by category", "Breakdown for the selected period (last 90 days).")
        chart_card_start()
        if analytics:
            data = {
                "Category": list(analytics.keys()),
                "Total": [analytics[c]["total_amount"] for c in analytics],
                "Percentage": [analytics[c]["percentage"] for c in analytics],
            }
            df_cat = pd.DataFrame(data).sort_values("Percentage", ascending=False)
            if df_cat.empty:
                empty_state("No expense data in this range.", "Add expenses to see the chart.")
            else:
                st.bar_chart(data=df_cat.set_index("Category")[["Percentage"]], use_container_width=True)
        else:
            empty_state("No category data in this range.", "Add expenses or widen the date range.")
        chart_card_end()

    with c2:
        chart_card("Monthly trend", "Total spending by month.")
        chart_card_start()
        if monthly_summary:
            df_m = pd.DataFrame(monthly_summary)
            df_m = df_m.rename(columns={"month_name": "Month", "total_amount": "Total"})
            df_m = df_m.sort_values("expense_month")
            if df_m.empty:
                empty_state("No monthly data yet.", "Add expenses to see the trend.")
            else:
                st.line_chart(data=df_m.set_index("Month")["Total"], use_container_width=True)
        else:
            empty_state("No monthly data yet.", "Add expenses to see the trend.")
        chart_card_end()
