import MySQLdb
import datetime

# Open database connection
db = MySQLdb.connect("localhost","root","root","crm" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
#INSERT INTO diary VALUES ( CURDATE( ) ,  'thursday',  'april',  '2017',  'Hello . rifat asdaj jkasdhjak .asdhdjk sdasdasd')
# Prepare SQL query to INSERT a record into the database.
now = datetime.datetime(2009,6,11)
str_now = str(now.date().isoformat())

#sql = """INSERT INTO diary (entry_date,day,month,year,content) VALUES ( %s,%s,%s,%s,%s),(str_now,'friday',  'april',  '2017',  'hjas asdjas')"""
sql="INSERT INTO diary (entry_date,content) VALUES ( %s,%s)"
args=str_now,'hello oedd'
try:
   # Execute the SQL command
   cursor.execute(sql,args)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
   print("error")
# disconnect from server
db.close()