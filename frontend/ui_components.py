"""
UI helper components and custom CSS for the Expense Tracking System.
Supports light and dark mode; theme is stored in st.session_state["theme"].
"""

import streamlit as st

# Session state key for theme: "light" | "dark"
THEME_SESSION_KEY = "theme"


def get_theme():
    """Returns current theme from session state. Default "light"."""
    return st.session_state.get(THEME_SESSION_KEY, "light")


def set_theme(theme: str):
    """Sets theme in session state. Use "light" or "dark"."""
    if theme in ("light", "dark"):
        st.session_state[THEME_SESSION_KEY] = theme


# =============================================================================
# LIGHT MODE CSS — stronger contrast so fonts are clearly visible
# =============================================================================
LIGHT_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #e2e8f0;
}

/* Main content area: soft but not blinding; all text dark for contrast */
[data-testid="stAppViewContainer"],
.block-container {
    background: #e2e8f0;
    color: #0f172a !important;
}
.block-container p, .block-container span, .block-container li,
[data-testid="stMarkdown"] p, [data-testid="stMarkdown"] span,
[data-testid="stMarkdown"] li, .stMarkdown p, .stMarkdown span {
    color: #0f172a !important;
}
[data-testid="stMarkdown"] label, .stMarkdown label,
h1, h2, h3, [data-testid="stHeader"] {
    color: #0f172a !important;
}
/* Captions and secondary text */
[data-testid="stCaptionContainer"] p, .stCaption {
    color: #475569 !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
}
[data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] p {
    color: #e2e8f0 !important;
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
    color: #f8fafc !important;
}
/* Sidebar has dark bg in both themes: keep toggle/labels light so "Dark mode" is visible */
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] label,
[data-testid="stSidebar"] label {
    color: #f8fafc !important;
    opacity: 1 !important;
}

.card-container {
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    border: 1px solid #cbd5e1;
    color: #0f172a !important;
}

[data-testid="stMetricValue"] {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: #0f172a !important;
}
[data-testid="stMetricLabel"] {
    font-size: 0.8rem !important;
    color: #475569 !important;
    text-transform: uppercase;
    letter-spacing: 0.02em;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 500;
    padding: 0.5rem 1.25rem;
    border: 1px solid #cbd5e1;
    background: #ffffff;
    color: #0f172a !important;
}
.stButton > button:hover {
    background: #f1f5f9;
    border-color: #94a3b8;
    color: #0f172a !important;
}
.stButton > button[kind="primary"] {
    background: #2563eb;
    border-color: #2563eb;
    color: #fff !important;
}
.stButton > button[kind="primary"]:hover {
    background: #1d4ed8;
    border-color: #1d4ed8;
    color: #fff !important;
}

.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    background: #ffffff !important;
    color: #0f172a !important;
}
.stSelectbox > div > div {
    border-radius: 8px;
}

[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label {
    color: #0f172a !important;
    opacity: 1 !important;
}

/* Date input: aligned box, consistent border and padding (light mode) */
[data-testid="stDateInput"] {
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    background: #ffffff !important;
    padding: 0.25rem 0.5rem !important;
}
[data-testid="stDateInput"] input {
    border: none !important;
    background: transparent !important;
}

.dataframe {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

/* Chart container: rounded corners, padding so graph sits inside (not touching edges) */
[data-testid="stVegaLiteChart"],
[data-testid="stVegaLiteChart"] > div,
.stVegaLiteChart,
[data-testid="stVegaLiteChart"] iframe {
    border-radius: 10px !important;
    overflow: hidden !important;
}
[data-testid="stVegaLiteChart"] {
    padding: 0 !important;
    background: #ffffff !important;
    border: 1px solid #e2e8f0;
    border-radius: 12px !important;
}
[data-testid="stVegaLiteChart"] iframe,
[data-testid="stVegaLiteChart"] > div {
    width: 100% !important;
    min-height: 100% !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: #cbd5e1;
    padding: 4px;
    border-radius: 10px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: 500;
    color: #0f172a !important;
}
.stTabs [aria-selected="true"] {
    background: #ffffff;
    color: #0f172a !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.08);
}

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px;
}
</style>
"""


# =============================================================================
# DARK MODE CSS — dark background, light text
# =============================================================================
DARK_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #0f172a;
    color: #f1f5f9 !important;
}

[data-testid="stAppViewContainer"],
.block-container {
    background: #0f172a !important;
    color: #f1f5f9 !important;
}
.block-container p, .block-container span, .block-container li,
[data-testid="stMarkdown"] p, [data-testid="stMarkdown"] span,
[data-testid="stMarkdown"] li, .stMarkdown p, .stMarkdown span {
    color: #f1f5f9 !important;
}
[data-testid="stMarkdown"] label, .stMarkdown label,
h1, h2, h3, [data-testid="stHeader"] {
    color: #f8fafc !important;
}
[data-testid="stCaptionContainer"] p, .stCaption {
    color: #94a3b8 !important;
}

/* View expenses + all main content: force light text (subheaders, paragraphs, labels) */
[data-testid="stAppViewContainer"] [data-testid="stVerticalBlock"] p,
[data-testid="stAppViewContainer"] [data-testid="stVerticalBlock"] span,
[data-testid="stAppViewContainer"] [data-testid="stVerticalBlock"] label,
[data-testid="stAppViewContainer"] [data-testid="stVerticalBlock"] h1,
[data-testid="stAppViewContainer"] [data-testid="stVerticalBlock"] h2,
[data-testid="stAppViewContainer"] [data-testid="stVerticalBlock"] h3,
[data-testid="stAppViewContainer"] [data-testid="stMarkdown"] p,
[data-testid="stAppViewContainer"] [data-testid="stMarkdown"] span,
[data-testid="stAppViewContainer"] [data-testid="stMarkdown"] label {
    color: #f1f5f9 !important;
}
[data-testid="stAppViewContainer"] [data-testid="stCaptionContainer"] p {
    color: #94a3b8 !important;
}

/* Date input in dark mode: full widget dark, no visible light box, aligned */
[data-testid="stDateInput"] {
    background: #1e293b !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
    padding: 0.25rem 0.5rem !important;
    overflow: hidden !important;
}
[data-testid="stDateInput"] input,
[data-testid="stDateInput"] div,
[data-testid="stDateInput"] button,
[data-testid="stDateInput"] span {
    background: #1e293b !important;
    color: #f1f5f9 !important;
    border-color: #475569 !important;
}
[data-testid="stDateInput"] input {
    border: none !important;
    background: transparent !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
}
[data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] p {
    color: #e2e8f0 !important;
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
    color: #f8fafc !important;
}
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] label,
[data-testid="stSidebar"] label {
    color: #f8fafc !important;
    opacity: 1 !important;
}

.card-container {
    background: #1e293b !important;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    border: 1px solid #334155;
    color: #f1f5f9 !important;
}
.card-container p {
    color: #e2e8f0 !important;
}

[data-testid="stMetricValue"] {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: #f8fafc !important;
}
[data-testid="stMetricLabel"] {
    font-size: 0.8rem !important;
    color: #94a3b8 !important;
    text-transform: uppercase;
    letter-spacing: 0.02em;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 500;
    padding: 0.5rem 1.25rem;
    border: 1px solid #475569;
    background: #1e293b !important;
    color: #f1f5f9 !important;
}
.stButton > button:hover {
    background: #334155 !important;
    border-color: #64748b;
    color: #f1f5f9 !important;
}
.stButton > button[kind="primary"] {
    background: #2563eb !important;
    border-color: #2563eb;
    color: #fff !important;
}
.stButton > button[kind="primary"]:hover {
    background: #1d4ed8 !important;
    border-color: #1d4ed8;
    color: #fff !important;
}

.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    border-radius: 8px;
    border: 1px solid #475569;
    background: #1e293b !important;
    color: #f1f5f9 !important;
}
.stSelectbox > div > div {
    border-radius: 8px;
}
/* Baseweb select/dropdown in dark mode */
[data-testid="stSelectbox"] div[role="listbox"],
[data-baseweb="select"] {
    background: #1e293b !important;
    color: #f1f5f9 !important;
}

[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label {
    color: #e2e8f0 !important;
    opacity: 1 !important;
}

/* Chart container: rounded corners, padding so graph sits inside (not touching edges) */
[data-testid="stVegaLiteChart"],
[data-testid="stVegaLiteChart"] > div,
.stVegaLiteChart {
    border-radius: 12px !important;
    overflow: hidden !important;
}
[data-testid="stVegaLiteChart"] {
    padding: 0 !important;
    background: #1e293b !important;
    border: 1px solid #334155 !important;
}
[data-testid="stVegaLiteChart"] iframe,
[data-testid="stVegaLiteChart"] > div {
    width: 100% !important;
    min-height: 100% !important;
}

/* DataFrames and tables */
[data-testid="stDataFrame"],
.dataframe {
    border-radius: 8px;
    overflow: hidden;
    background: #1e293b !important;
    border: 1px solid #334155;
}
[data-testid="stDataFrame"] td,
[data-testid="stDataFrame"] th,
[data-testid="stDataFrame"] span,
[data-testid="stDataFrame"] div {
    color: #f1f5f9 !important;
}
[data-testid="stDataFrame"] td,
[data-testid="stDataFrame"] th {
    background: #1e293b !important;
    border-color: #334155 !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: #1e293b;
    padding: 4px;
    border-radius: 10px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: 500;
    color: #94a3b8 !important;
}
.stTabs [aria-selected="true"] {
    background: #334155 !important;
    color: #f8fafc !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.2);
}

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px;
}

/* Expander and other widgets */
[data-testid="stExpander"] {
    background: #1e293b !important;
    border: 1px solid #334155;
    color: #f1f5f9 !important;
}
</style>
"""


def inject_custom_css():
    """Inject theme-dependent CSS. Call after theme is set (e.g. in app.py)."""
    theme = get_theme()
    css = DARK_CSS if theme == "dark" else LIGHT_CSS
    st.markdown(css, unsafe_allow_html=True)


def section_header(title: str, description: str = ""):
    """Renders section header and optional description (always visible)."""
    st.subheader(title)
    if description:
        st.caption(description)


def render_metric_card(label: str, value: str, delta: str = None, delta_color: str = "normal"):
    """Renders a metric. delta_color: "normal" | "inverse" | "off"."""
    st.metric(label=label, value=value, delta=delta, delta_color=delta_color)


def chart_card(title: str, description: str = ""):
    """Section header for a chart."""
    section_header(title, description)


def chart_card_start():
    """Opens a card container div. Pair with chart_card_end() after content."""
    st.markdown('<div class="card-container">', unsafe_allow_html=True)


def chart_card_end():
    """Closes the card container div opened by chart_card_start()."""
    st.markdown("</div>", unsafe_allow_html=True)


def _empty_state_colors():
    """Returns (message_color, subtext_color) for current theme."""
    if get_theme() == "dark":
        return "#e2e8f0", "#94a3b8"
    return "#475569", "#64748b"


def empty_state(message: str, subtext: str = ""):
    """Renders an empty state. Colors adapt to light/dark theme."""
    msg_color, sub_color = _empty_state_colors()
    st.markdown(
        f"""
        <div class="card-container" style="text-align: center; padding: 2rem;">
            <p style="color: {msg_color}; font-size: 1rem; margin-bottom: 0.5rem;">{message}</p>
            <p style="color: {sub_color}; font-size: 0.875rem;">{subtext}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def wrap_in_card(contents_markdown: str = ""):
    """Wraps HTML/markdown in a card container."""
    st.markdown(
        f'<div class="card-container">{contents_markdown}</div>',
        unsafe_allow_html=True,
    )
