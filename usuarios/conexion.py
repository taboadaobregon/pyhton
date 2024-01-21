import mysql.connector

def conectar():
    database = mysql.connector(
        host="localhost",
        user="root",
        password="",
        database="senati",
        port=3306,
    )

    cursor = database.cursor(buffered=True)
    return [database,cursor]