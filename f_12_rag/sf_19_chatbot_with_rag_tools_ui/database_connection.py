import sqlite3

def create_connection():
    '''Create a connection to SQLite database'''

    conn = sqlite3.connect('chatbot_checkpoint.db', check_same_thread=False)

    return conn