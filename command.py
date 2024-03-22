import mysql.connector

cnx = mysql.connector.connect(user='root',password='M2048*Nepal',
                              host='127.0.0.1',
                              database='sys')
cnx.close()
