#!/usr/bin/env /Applications/MAMP/Library/bin/python
# connect to MySQL database via MAMP
import mysql.connector
from mysql.connector import errorcode


# connect to MySQL database
def connect():
    try:
        cnx = mysql.connector.connect(user='root', password='root', host='localhost',
                                      unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock')
        print("Connected to MySQL database")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


# main function
def main():
    connect()


# call main function
if __name__ == "__main__":
    main()

# create a database in MySQL database via MAMP
import mysql.connector
from mysql.connector import errorcode

