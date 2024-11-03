import mysql.connector
def get_data():
    mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="fldb")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM todo")
    result=mycursor.fetchall()
    mydb.close()
    return result