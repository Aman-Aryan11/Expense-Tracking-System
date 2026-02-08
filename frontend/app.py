"""
Expense Tracking System — Streamlit UI entry point.
Dashboard-style layout: sidebar + main area with tabs. All logic lives in tab modules.
"""

import streamlit as st
from ui_components import inject_custom_css, get_theme, set_theme, THEME_SESSION_KEY
from dashboard import dashboard_tab
from add_update import add_update_tab
from view_expenses import view_expenses_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab

# ----- Page config (must be first Streamlit call) -----
st.set_page_config(
    page_title="Expense Tracking System",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----- Theme: init session state and sidebar toggle -----
if THEME_SESSION_KEY not in st.session_state:
    st.session_state[THEME_SESSION_KEY] = "light"

with st.sidebar:
    st.title("💰 Expense Tracker")
    st.caption("Track spending by date and category.")
    st.markdown("---")
    dark = st.toggle("Dark mode", value=(get_theme() == "dark"), help="Switch to dark theme for better visibility at night.")
    if dark != (get_theme() == "dark"):
        set_theme("dark" if dark else "light")
        st.rerun()
    st.markdown("---")
    st.caption("Use the tabs to switch between Dashboard, Add Expense, View, and Analytics.")

# ----- Theme-dependent CSS -----
inject_custom_css()

# ----- Main area: section title + tabs -----
st.title("Expense Tracking System")
st.caption("Dashboard, add or view expenses, and analyze spending.")

tab_dashboard, tab_add, tab_view, tab_analytics = st.tabs([
    "Dashboard",
    "Add Expense",
    "View Expenses",
    "Analytics",
])

with tab_dashboard:
    dashboard_tab()

with tab_add:
    add_update_tab()

with tab_view:
    view_expenses_tab()

with tab_analytics:
    # Sub-tabs for Analytics: By Category | By Months
    sub_cat, sub_months = st.tabs(["By category", "By months"])
    with sub_cat:
        analytics_category_tab()
    with sub_months:
        analytics_months_tab()
