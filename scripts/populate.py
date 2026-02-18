import mysql.connector
import sys
sys.path.insert(0,"../PAMS")

import dbSecrets

try:
    mydb = mysql.connector.connect(
        host = dbSecrets.devHost,
        user = dbSecrets.devUser,
        password = dbSecrets.devPassword,
        dbname = dbSecrets.devName
    )
    print("Database connection successful:", mydb)
    mydb.close()
except mysql.connector.Error as err:
    print("Error: ", err)
    sys.exit(1)