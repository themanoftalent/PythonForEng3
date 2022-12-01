connecting to mysql via Python 
>
> I am trying to connect to a mysql database via Python. I have the
> following code:
>
> import MySQLdb
> import sys
> from MySQLdb import *

def connect_mysql():
    try:
        db = MySQLdb.connect(host="localhost", user='root',passwd='root',db='test')
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        
        print "Database version : %s " % data
        
        
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
        
    finally:
        if db:
            db.close()
            
if __name__ == "__main__":
    connect_mysql()
    
