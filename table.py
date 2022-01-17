import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" #The interger primary key is used when you want to create autoincrementing columns
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price int, store_id int)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS stores (id INTEGER PRIMARY KEY, name text)"
cursor.execute(create_table)

connection.commit()

connection.close()