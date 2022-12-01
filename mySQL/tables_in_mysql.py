import mysql.connector
from mysql.connector import errorcode


# create table in MYSQL SCHOOL database
def create_table(cursor, table_name):
    try:
        cursor.execute("CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), "
                       "age INT)".format(table_name))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


# main function
def main():
    cnx = mysql.connector.connect(user = 'root', password = 'root', host = 'localhost',
                                    unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock')

    cursor = cnx.cursor()
    cursor.execute("USE SCHOOL")
    create_table(cursor, "STUDENTS")
    cursor.close()
    cnx.close()
    

# call main function
if __name__ == "__main__":
    main()
