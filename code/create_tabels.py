import sqlite3

connection = sqlite3.connect('mydatabase.db')

cursor = connection.cursor()

create_user_tabel = "CREATE TABLE if NOT EXISTS user (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_user_tabel)

create_item_tabel = "CREATE TABLE IF NOT EXISTS items (name text, price text)"
cursor.execute(create_item_tabel)

text_data = "INSERT INTO items VALUES ('test', 10.99)"
cursor.execute(text_data)

test_user = "INSERT INTO users VALUES(1, 'user', 'password')"
text_data = "insert into ITEMS values('TEXT', 10.99)"
cursor.execute(text_data)
cursor.execute(test_user)

connection.commit()

connection.close()