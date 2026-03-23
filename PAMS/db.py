import sys
import random

import mysql.connector
from mysql.connector import errorcode

from dbSecrets import *

from ErrorBoxes import ErrorMessage

isUsingDev = True

host = ""
user = ""
password = ""
dbName = ""

def GetConnection():
    if isUsingDev:
        host = devHost
        user = devUser
        password = devPassword
        dbName = devName
    else: 
        host = prodHost
        user = prodUser
        password = prodPassword
        dbName = prodName

    try:
        conn = mysql.connector.connect(host = host, user = user, password =password)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('User name or password is not working')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        if conn.is_connected():
            print('MySQL Connection is established')
            return conn


def GetTenants():

    query = "SELECT * FROM tenants"

    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query)
    records = dbcursor.fetchall()
    conn.commit()

    conn.close()
    dbcursor.close()
    print("Closed Database")
    return records

def GetLocations():

    query = "SELECT * FROM locations"

    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query)
    records = dbcursor.fetchall()
    conn.commit()

    conn.close()
    dbcursor.close()
    print("Closed Database")
    return records

# Gets all the headers from a table in the database
def GetHeaders(table : str):
    query = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = %s;"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")
    dbcursor.execute(query, (table,))
    headers = dbcursor.fetchall()
    dbcursor.close()
    conn.close()
    print("Closed Database")
    return headers

def CheckEmailIsValid(email : str):
    query = "SELECT * FROM tenants WHERE email = %s"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")
    dbcursor.execute(query, (email,))
    user = dbcursor.fetchone()
    
    if user is not None:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        title = "Tenant Already Exists"
        description = "This email has already been used to sign up a user. Please try a different email."
        error = ErrorMessage(title, description)
        return (error)
    else:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        return None

#This assumes that the email has already been checked
def SignUpUser(fName : str, lName : str, email : str, password : str, NINumber : str, phoneNum : int, job: str):
    #TODO do SQL injection protection
    query = "INSERT INTO tenants (first_name,last_name,national_insurance, email,password,phone_number,occupation) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query, (fName,lName,NINumber,email,password,phoneNum,job,))
    conn.commit()


    conn.close()
    dbcursor.close()
    print("Closed Database")
    return None

def LoginUser(email : str, hashedPassword : str):
    query = "SELECT * FROM tenants WHERE email = %s AND password =%s"
    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query, (email, password ,))
    tenant = dbcursor.fetchone()
    if tenant is None:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        title = "Failure To Login"
        description = "No user matches the credentials provided."
        error = ErrorMessage(title, description)
        return (error)
    else:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        return None

def fetch_notifications(tenant_id=None, location_id=None):

    conn = GetConnection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('USE {};'.format(devName))

    query = """
    SELECT notification_id, subject, message, is_read, created_at
    FROM notifications
    """

    conditions = []
    params = []

    if tenant_id:
        conditions.append("tenant_id = %s")
        params.append(tenant_id)

    if location_id:
        conditions.append("location_id = %s")
        params.append(location_id)

    if conditions:
        query += " WHERE " + " OR ".join(conditions)
    else:
        return []

    query += " ORDER BY created_at DESC"

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results


def mark_notification_as_read(notification_id):

    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute('USE {};'.format(devName))

    cursor.execute(
        "UPDATE notifications SET is_read = 1 WHERE notification_id = %s",
        (notification_id,)
    )

    conn.commit()
    conn.close()