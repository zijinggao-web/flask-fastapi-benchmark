import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test_db",
    port=3306
)


with conn.cursor() as cursor:
    cursor.execute("SELECT 1")
    print(cursor.fetchone())

conn.close()
