-- Schema for Bluestock Mutual Fund Capstone Project

-- 1. Table to store general information about each mutual fund scheme
CREATE TABLE IF NOT EXISTS scheme_metadata (
    scheme_code INTEGER PRIMARY KEY,
    scheme_name TEXT NOT NULL,
    isin_growth TEXT,
    isin_div_reinvest TEXT,
    scheme_category TEXT,
    scheme_type TEXT -- Open-Ended vs Close-Ended
);

-- 2. Table to store historical NAV data (This is where our cleaned data goes!)
CREATE TABLE IF NOT EXISTS historical_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    nav_date DATE NOT NULL,
    nav_value REAL NOT NULL,
    FOREIGN KEY (scheme_code) REFERENCES scheme_metadata(scheme_code),
    UNIQUE(scheme_code, nav_date) -- Prevents duplicate entries for the same day
);