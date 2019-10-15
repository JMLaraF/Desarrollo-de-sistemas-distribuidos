import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="m0th3l3td3lg4"
)

mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE IF NOT EXISTS Central")
mydb.cmd_reset_connection

mydb2 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="m0th3l3td3lg4",
    database="Central"
)

mycursor = mydb2.cursor()


mycursor.execute("CREATE TABLE Sumas (resultado INTEGER, ip VARCHAR(25), hora TIME)")