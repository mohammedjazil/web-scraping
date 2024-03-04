import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="jazil_usr",
    password="Jazil@1233",
    database ="store" 
)
cursor = mydb.cursor()

# cursor.execute("CREATE TABLE names_tbl (id INT AUTO_INCREMENT PRIMARY KEY,name varchar(255),age INT)")

# query = "INSERT INTO names_tbl (name,age) VALUES (%s,%s)"
# values = [
#     ("john",32),
#     ("alice",12),
#     ("frank",23),
#     ("grace",54),
#     ("eva",13),
#     ("sanjay",26),
#     ("rohit",45),
#     ("yasin",24),
#     ("fayis",58),
#     ]

# cursor.executemany(query,values)
mydb.commit()

cursor.execute("SELECT * FROM names_tbl where age>25")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
mydb.close()