import mysql.connector
from mysql.connector import errorcode


# fill the student table with name and age data
def fill_studentsTable(cursor, table_name):
    try:
        # id, name, age
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (108,'Jack', 20)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (109,'Jill', 21)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (110,'John', 22)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (111,'Jane', 23)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (112,'Joe', 24)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (113,'Jen', 25)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (114,'Jim', 26)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (115,'Jenny', 27)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (116,'Jill', 28)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (117,'Jill', 29)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (118,'Jill', 30)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (119,'Jill', 31)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (120,'Jill', 32)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (121,'Jill', 33)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (122,'Jill', 34)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (123,'Jill', 35)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (124,'Jill', 36)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (125,'Jill', 37)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (126,'Jill', 38)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (127,'Jill', 39)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (128,'Jill', 40)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (129,'Jill', 41)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (130,'Jill', 42)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (131,'Jill', 43)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (132,'Jill', 44)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (133,'Jill', 45)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (134,'Jill', 46)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (135,'Jill', 47)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (136,'Jill', 48)".format(table_name))
        cursor.execute("INSERT INTO {} (id,name, age) VALUES (137,'Jill', 49)".format(table_name))

    except mysql.connector.Error as err:
        print("Failed inserting record: {}".format(err))
        exit(1)


# main function
def main():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost',
                                  unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock')
    cursor = cnx.cursor()
    cursor.execute("USE SCHOOL")
    fill_studentsTable(cursor, "STUDENTS")
    cnx.commit()
    cursor.close()
    cnx.close()


# call main function
if __name__ == "__main__":
    main()
