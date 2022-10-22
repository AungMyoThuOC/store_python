import sqlite3

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()

create_user_tabel = "CREATE TABLE if NOT EXISTS user (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_user_tabel)

create_item_tabel = "CREATE TABLE IF NOT EXISTS items (name text, price text)"
cursor.execute(create_item_tabel)

text_data = "INSERT INTO items VALUES ('test', 10.99)"
cursor.execute(text_data)

connection.commit()

connection.close()