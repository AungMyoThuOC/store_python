import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    database = "winterfell",
    user = "jonsnow",
    password = "ghost123"
)

cursor = connection.cursor()

#SQL Query or SQL Command
create_table = "CREATE TABLE IF NOT EXISTS users(id intger PRINARY kEY, username text, password text)"

#set
user = (1, "Onii Chan", "12345678")
create_user_query = "INSERT INTO users VALUES(?, ?, ?)"

#cursor.execute(create_user_query, user)

create_user_query_new = """INSERT INTO users VALUES (2, "Onii", "Chan")"""
#cursor.execute(create_table)
#cursor.execute(create_user_query_new)

users = [
    (3, "Jon", "ghost123")
    (4, "snow", "kinginthenorth")
]

#cursor.executemany(create_user_query, users)

select_query = "SELECT * FROM users WHERE id = 4"
for data in cursor.execute(select_query):
    if data is None:
        print("User not Found")
    else: 
        print(data)

connection.commit()

connection.close()