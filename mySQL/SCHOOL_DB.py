import mysql.connector
from mysql.connector import errorcode


# create a database
def create_database(cursor, database_name):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


# main function
def main():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost',
                                  unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock')
    cursor = cnx.cursor()
    create_database(cursor, "SCHOOL")
    cursor.close()
    cnx.close()
    cursor = cnx.cursor()
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)
    create_database(cursor, "SCHOOL")
    cursor.close()
    cnx.close()


# call main function
if __name__ == "__main__":
    main()
