import sqlite3
import datetime
import pandas as pd

def init_db():
    conn = sqlite3.connect("chatbot.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user TEXT,
            bot TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(user_msg, bot_msg):
    conn = sqlite3.connect("chatbot.db")
    cur = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO conversations (timestamp, user, bot) VALUES (?, ?, ?)",
                (timestamp, user_msg, bot_msg))
    conn.commit()
    conn.close()

def export_chat():
    try:
        conn = sqlite3.connect("chatbot.db")
        df = pd.read_sql_query("SELECT * FROM conversations", conn)
        df.to_csv("chat_history.csv", index=False)
        conn.close()
        return "Exported to chat_history.csv"
    except Exception as e:
        return f"Error: {e}"