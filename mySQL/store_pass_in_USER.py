import mysql.connector
from mysql.connector import errorcode

# store password and username in a table USERS in a database named SCHOOL in mysql server

# connect to mysql server
try:
    cnx = mysql.connector.connect(user = 'root', password = 'root', host = 'localhost',
                                  unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock')

    # create a cursor
    cursor = cnx.cursor()

    # create a database named SCHOOL
    try:
        cursor.execute('CREATE DATABASE SCHOOL')
    except mysql.connector.Error as err:
        print('Failed creating database: {}'.format(err))
        exit(1)

    # connect to the database
    cnx.database = 'SCHOOL'

    # create a table USERS
    try:
        cursor.execute('CREATE TABLE USERS (username VARCHAR(20), password VARCHAR(20))')
    except mysql.connector.Error as err:
        print('Failed creating table: {}'.format(err))
        exit(1)

    # insert a row into the table
    try:
        cursor.execute('INSERT INTO USERS (username, password) VALUES (%s, %s)', ('root', ' root')) # insert a row into the table
    except mysql.connector.Error as err:
        print('Failed inserting data: {}'.format(err))
        exit(1)

    # commit the changes
    cnx.commit()

    # close the cursor
    cursor.close()

    # close the connection
    cnx.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Database does not exist')
    else:
        print(err)
else:
    cnx.close()

