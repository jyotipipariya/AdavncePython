import pymysql
import UserBean
from UserBean import *
class UserDao():

    def nextPk(self):
        result = " "
        pk = 0
        connection = pymysql.connect(host="localhost", user="root", password="root", db="company", port=3306)
        with connection.cursor() as cursor:
            sql = "select max(id) from user"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.close()
            for d in result:
                pk = d[0]
        return pk+1

    def add(self, ub):
        pk = UserDao.nextPk(self)
        connection = pymysql.connect(host="localhost", user="root", password="root", db="company", port=3306)
        with connection.cursor() as cursor:
            sql = "insert into user values(%s, %s, %s, %s, %s, %s, %s)"
            data = (pk, ub.getFirst_name(), ub.getLast_name(), ub.getDOB(), ub.getemail_id(), ub.getPassword(),ub.getMobile())
            cursor.execute(sql, args=data)
            connection.commit()
        connection.close()

    def getById(self, id):
        result = " "
        connection = pymysql.connect(host="localhost", user="root", password="root", db="company", port=3306)
        with connection.cursor() as cursor:
            sql = "select * from user where id = (%s)"
            data = (id)
            cursor.execute(sql, args=data)
            result = cursor.fetchall()
            connection.close()
            print("Id", '\t', "First_name,"'\t', "Last_name", '\t', "DOB", '\t', "email_id", '\t', "Password", '\t', "Mobile")
            for d in result:
                print(d[0], '\t', d[1], '\t', d[2], '\t', d[3], '\t', d[4], d[5], '\t', d[6])

    def update(self, ub):
        connection = pymysql.connect(host="localhost", user="root", password="root", db="company", port=3306)
        with connection.cursor() as cursor:
            sql = "update user set First_name = (%s), Last_name = (%s), DOB = (%s), email_id = (%s), Password = (%s), Mobile = (%s) where id = (%s)"
            data = (ub.getFirst_name(), ub.getLast_name(), ub.getDOB(), ub.getemail_id(), ub.getpassword(), ub.getmobile(), ub.getId())
            cursor.execute(sql, args=data)
            connection.commit()
        connection.close()



