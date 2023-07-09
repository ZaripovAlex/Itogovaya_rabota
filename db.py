import mysql.connector
from mysql.connector import Error
from os import getenv
from pathlib import Path

SOURCE = getenv('SOURCE')
LOGIN = getenv('LOGIN')
PASSWORD = getenv('PASSWORD')


def create_connection() -> mysql.connector:
    connection = None
    try:
        connection = mysql.connector.connect(
            host=SOURCE,
            user=LOGIN,
            passwd=PASSWORD
        )
        print("Подключение к MYSQL прошло успешно")
    except Error as e:
        print(f"Ошибка: {e}")
    return connection


def create_tables():
    cursor = create_connection().cursor()

    try:

        cursor.execute("""CREATE TABLE IF NOT EXISTS home_animals (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                command TEXT,
                                birthday TEXT
                            )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS farm_animals (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                command TEXT,
                                birthday TEXT
                            )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS young_animals (
                                id INTEGER PRIMARY KEY,
                                animal_id INTEGER,
                                months INTEGER,
                                FOREIGN KEY (animal_id) REFERENCES home_animals(id) 
                            )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS animals (
                                id INTEGER PRIMARY KEY,
                                animal_id INTEGER,
                                animal_type TEXT,
                                previous_table TEXT,
                                FOREIGN KEY (animal_id) REFERENCES domestic_animals(id) 
                            )""")
        print("Таблицы созданы")
    except Error as e:
        print(f"Ошибка: {e}")


def insert_record(table, data):
    db = create_connection()
    cursor = db.cursor()
    try:
        if table == 1:
            cursor.execute("INSERT INTO home_animals (name, command, birthday) VALUES (?, ?, ?)", data)
        if table == 2:
            cursor.execute("INSERT INTO farm_animals (name, command, birthday) VALUES (?, ?, ?)", data)
        cursor.close()
        print("Запись добавлена!")
    except Error as e:
        print(f"Ошибка: {e}")


def delete_record(table, id):
    db = create_connection()
    cursor = db.cursor()
    try:
        if table == 1:
            cursor.execute("DELETE FROM home_animals WHERE id=?", (id,))
        if table == 2:
            cursor.execute("DELETE FROM farm_animals WHERE id=?", (id,))
        cursor.close()
        print("Запись удалена")
    except Error as e:
        print(f"Ошибка: {e}")


def view_records(table):
    db = create_connection()
    cursor = db.cursor()
    try:
        if table == 1:
            cursor.execute("SELECT * FROM home_animals")
            date = cursor.fetchall()
            for i in date:
                print(i)
        if table == 2:
            cursor.execute("SELECT * FROM farm_animals")
            date = cursor.fetchall()
            for i in date:
                print(i)
    except Error as e:
        print(f"Ошибка: {e}")


def search_records(table, keyword):
    db = create_connection()
    cursor = db.cursor()
    if table == 1:
        cursor.execute("SELECT * FROM home_animals WHERE name LIKE ? OR command LIKE ?",
                       ('%' + keyword + '%', '%' + keyword + '%'))
        date = cursor.fetchall()
        for i in date:
            print(i)
    if table == 2:
        cursor.execute("SELECT * FROM farm_animals WHERE name LIKE ? OR command LIKE ?",
                       ('%' + keyword + '%', '%' + keyword + '%'))
        date = cursor.fetchall()
        for i in date:
            print(i)
