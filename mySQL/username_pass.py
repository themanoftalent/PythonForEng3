import mysql.connector
from mysql.connector import errorcode


# create a username and password store in mysql USERNAMES table
# and use it to connect to mysql database

# CREATE TABLE USERS (username VARCHAR(255), password VARCHAR(255));
def create_table(cursor, table_name):
    try:
        cursor.execute("CREATE TABLE {} (username VARCHAR(255), password VARCHAR(255))".format(table_name))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


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
    create_table(cursor, "USERS")
    insert_user_pass(cursor, "root", "root")
    cursor.close()
    cnx.close()


if __name__ == "__main__":
    main()


def get_user_pass():
    try:
        cnx = mysql.connector.connect(user='root', password='root', host='localhost',
                                      unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock')

        cursor = cnx.cursor()
        cursor.execute("USE SCHOOL")
        cursor.execute("SELECT * FROM USERS")
        for (username, password) in cursor:
            print("{} {}".format(username, password))
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


def main():
    get_user_pass()


if __name__ == "__main__":
    main()
