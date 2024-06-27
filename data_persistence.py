import sqlite3


def save_conversation(conversation, db_connection):
    conn = sqlite3.connect(db_connection)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS conversations
                      (id INTEGER PRIMARY KEY, conversation TEXT)''')

    cursor.execute("INSERT INTO conversations (conversation) VALUES (?)",
                   (str(conversation),))

    conn.commit()
    conn.close()
