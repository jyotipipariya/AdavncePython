import pymysql
conn = pymysql.connect(host="localhost", user="root", password="root", db="sunrays", port=3306)
with conn.cursor() as cursor:
    sql = "insert into part values(11, 'Gear', 'Silver', 2)"
    cursor.execute(sql)
    conn.commit()
conn.close()
