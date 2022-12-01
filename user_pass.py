import mysql.connector
from mysql.connector import errorcode

# store password and username in a table USERS in a database named SCHOOL in mysql server

# connect to mysql server
try:
    cnx = mysql.connector.connect(user='root', password='root', host='localhost',
                                  unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock')

    cursor = cnx.cursor()
    cursor.execute("USE SCHOOL")
    # use USERS table to store username and password
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


