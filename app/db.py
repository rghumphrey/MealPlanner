# app/db.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "meals.db"

def get_connection():
    """Return a SQLite connection (with row factory for dict-like access)."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables if they don't exist."""
    conn = get_connection()
    cur = conn.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        calories REAL,
        protein REAL,
        carbs REAL,
        fat REAL,
        fiber REAL,
        store TEXT,
        price REAL,
        serving_size REAL,
        serving_unit TEXT,
        longevity_days INTEGER,
        tags TEXT
    );
    CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    );
    CREATE TABLE IF NOT EXISTS meal_ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meal_id INTEGER,
        ingredient_id INTEGER,
        quantity REAL,
        FOREIGN KEY (meal_id) REFERENCES meals (id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredients (id)
    );
    """)
    conn.commit()
    conn.close()
