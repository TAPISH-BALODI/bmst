import pymysql

try:
    connection = pymysql.connect(
        db='busdb',
        user='root',
        passwd='Dt734*26',
        host='127.0.0.1',
        port=3306
    )
    print("Connected to MySQL database successfully!")
    # Perform database operations here
    # ...
except pymysql.Error as e:
    print("Error connecting to MySQL database:", e)