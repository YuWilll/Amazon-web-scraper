import sqlite3

def as_sql(catalogue):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            price REAL,
            rating REAL,
            reviews INTEGER,
            name TEXT,
            link TEXT
        )
    ''')
    conn.commit()

    for item in catalogue:
        cursor.execute('''
            INSERT INTO products (price, rating, reviews, name, link)
            VALUES (:price, :rating, :reviews, :name, :link)
        ''', item)
        
    conn.commit()
    conn.close()

def products_with(word, db_path='products.db'):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Makes all rows act as dicts
    cursor = conn.cursor()

    query = "SELECT * FROM products WHERE name LIKE ?"
    cursor.execute(query, (f'%{word}%',))
    items = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return items

def products_without(word, db_path='products.db'):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Makes all rows act as dicts
    cursor = conn.cursor()

    query = "SELECT * FROM products WHERE name NOT LIKE ?"
    cursor.execute(query, (f'%{word}%',))
    items = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return items
