import mysql.connector
   
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "123456", database = "mydb")
 
# in đối tượng connection ra màn hình
print(myconn)
 
# tạo đối tượng cursor
cur = myconn.cursor()
 
# in đối tượng cursor ra màn hình
print(cur)  