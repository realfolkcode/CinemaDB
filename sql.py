import mysql.connector
from mysql.connector import MySQLConnection, Error

connect_config = {'host': 'localhost',
                  'database': 'pokupka_biletov',
                  'user' : 'root',
                  'password': 'myrootpassword'}


def query_with_fetchone(query):
    try:
        conn = mysql.connector.connect(**connect_config)
        cursor = conn.cursor()
        cursor.execute(query)

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def query_with_fetchall(query):
    rows = []
    try:
        conn = mysql.connector.connect(**connect_config)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
        return rows


def insert(query):
    id = -1
    try:
        conn = mysql.connector.connect(**connect_config)
        cursor = conn.cursor()
        cursor.execute(query)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
            id = cursor.lastrowid
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
        return id