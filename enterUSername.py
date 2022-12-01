import mysql.connector
from mysql.connector import errorcode

def insert_user_pass(cursor, username, password):
    try:
        cursor.execute("INSERT INTO USERS (username, password) VALUES (%s, %s)", (username, password))
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print("OK")


def main():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost',
                                  unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock')

    cursor = cnx.cursor()
    cursor.execute("USE SCHOOL")
    insert_user_pass(cursor, "cemils", "root123")
    cursor.close()
    cnx.close()


if __name__ == "__main__":
    main()
