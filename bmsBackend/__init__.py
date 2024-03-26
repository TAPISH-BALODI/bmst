import pymysql

try:
    connection = pymysql.connect(
        db='busdb',
        user='root',
        passwd='Dt734*26',
        host='localhost',
        port=3306
    )
    print("Connected to MySQL database successfully!")
    # Perform database operations here
    # ...
except pymysql.Error as e:
    print("Error connecting to MySQL database:", e)