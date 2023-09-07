import sqlite3
import hashlib

cx = sqlite3.connect("accountData.db")
cu = cx.cursor()

cu.execute("""
CREATE TABLE IF NOT EXISTS AccountData (
    id INTEGER PRIMARY KEY,
    AccountName VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL
)
""")

cx.commit()
