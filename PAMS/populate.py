import mysql.connector
from dbSecrets import *

try: 
    mydb = mysql.connector.connect( 
        host = devHost,
        user = devUser,
        password = devPassword,
        database = devName
    )
    print(mydb)
    print("Database connection successful")
except mysql.connector.Error as err:
    print("Error connecting to MySQL:", err)
mydb.close()
