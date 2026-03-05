import sqlite3

def create_connection():
    '''Create a connection to the SQLite database.'''

    conn = sqlite3.connect('chatbot_checkpoints.db', check_same_thread=False)

    return conn
