import sqlite3

def save_request(request):
    db_table = sqlite3.connect('requests.db')
    db_table.execute('''
        CREATE TABLE IF NOT EXISTS requests_from_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request TEXT
        )
    ''')
    db_table.execute('INSERT INTO requests_from_users (request) VALUES (?)', (request,))
    db_table.commit()
    db_table.close()
