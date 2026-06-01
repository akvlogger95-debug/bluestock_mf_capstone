import sqlite3
import pandas as pd
import streamlit as st
from pathlib import Path

# Set up the page layout
st.set_page_config(page_title="Bluestock MF Analytics", layout="wide")

st.title("📊 Bluestock Mutual Fund Analytics Dashboard")
st.markdown("Interactive performance monitoring portal.")

# Resolve database path dynamically
BASE_DIR = Path(__file__).resolve().parent.parent
db_file = BASE_DIR / "data" / "db" / "bluestock_mf.db"

# Connect and read from our database
if db_file.exists():
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("SELECT nav_date, nav_value FROM historical_nav ORDER BY nav_date ASC;", conn, parse_dates=['nav_date'])
    conn.close()
    
    if not df.empty:
        # Create metric view cards
        latest_nav = df['nav_value'].iloc[-1]
        earliest_nav = df['nav_value'].iloc[0]
        
        col1, col2 = st.columns(2)
        col1.metric(label="Latest NAV Value", value=f"INR {latest_nav:.2f}")
        col2.metric(label="Total Data Records Available", value=f"{len(df)} Days")
        
        # Interactive Plotly time series chart
        st.subheader("📈 Net Asset Value (NAV) Lifetime History")
        st.line_chart(df.set_index('nav_date')['nav_value'])
    else:
        st.warning("Database exists but contains no records yet.")
else:
    st.error(f"Database file not found at: {db_file}")