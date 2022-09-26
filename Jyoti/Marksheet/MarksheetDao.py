import pymysql
import MarksheetBean
from MarksheetBean import *
class MarksheetDao():

    def nextPk(self):
        result = " "
        pk = 0
        connection = pymysql.connect(host="localhost", user="root", password="root", db="sunrays", port=3306)
        with connection.cursor() as cursor:
            sql = "select max(id) from marksheet"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.close()
            for d in result:
                pk = d[0]
        return pk+1

    def add (self,mb):
        pk = MarksheetDao.nextPk(self)
        connection = pymysql.connect(host="localhost", user="root", password="root", db="sunrays")
        with connection.cursor() as cursor:
            sql = "insert into marksheet values(%s, %s, %s, %s, %s)"
            data = (pk, mb.getName(), mb.getPhysics(), mb.getChemistry(),mb.getMaths())
            cursor.execute(sql,args=data)
            connection.commit()
        connection.close()

    def update(self,mb):
        connection = pymysql.connect(host="localhost", user="root", password="root", db="sunrays", port=3306)
        with connection.cursor() as cursor:
            sql = "update marksheet set name = (%s), Physics = (%s), Chemistry = (%s), Maths = (%s) where id = (%s)"
            data = (mb.getName(), mb.getPhysics(), mb.getChemistry(), mb.getMaths(), mb.getId())
            cursor.execute(sql,args=data)
            connection.commit()
        connection.close()

    def delete(self, id):
        result = " "
        connection = pymysql.connect(host="localhost", user="root", password="root", db="sunrays", port=3306)
        with connection.cursor() as cursor:
            sql = "delete from marksheet where id = (%s)"
            data = (id)
            cursor.execute(sql, args = data)
            connection.commit()
        connection.close()

    def getById(self,id):
        result = " "
        connection = pymysql.connect(host="localhost", user="root", password="root", db="sunrays", port=3306)
        with connection.cursor() as cursor:
            sql = "select * from marksheet where id = (%s)"
            data = (id)
            cursor.execute(sql, args=data)
            result = cursor.fetchall()
        connection.close()
        print("Id",'\t', "Name,"'\t', "Physics",'\t',"Chemistry",'\t', "Maths",)
        for d in result:
            print(d[0],'\t', d[1],'\t', d[2],'\t', d[3],'\t', d[4])

    def findByName(self, name):
        result = " "
        connection = pymysql.connect(host="localhost", user="root", password="root", db="sunrays", port=3306)
        with connection.cursor() as cursor:
            sql = "select * from marksheet where name = (%s)"
            data = (name)
            cursor.execute(sql, args=data)
            result = cursor.fetchall()
        connection.close()
        print("Id", '\t', "Name,"'\t', "Physics", '\t', "Chemistry", '\t', "Maths", )
        for d in result:
            print(d[0], '\t', d[1], '\t', d[2], '\t', d[3], '\t', d[4])

    def search(self):
        result = " "
        connection = pymysql.connect(host="localhost", user="root", password="root", db="sunrays", port=3306)
        with connection.cursor() as cursor:
            sql = "select * from marksheet"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.close()
            print("Id", '\t', "Name", '\t', "Physics", '\t', "Chemistry", '\t', "Maths", )
            for d in result:
                print(d[0], '\t', d[1], '\t', d[2], '\t', d[3], '\t', d[4])


    def getMeritList(self):
        result = " "
        connection = pymysql.connect(host="localhost", user="root", password="root", db="sunrays", port=3306)
        with connection.cursor() as cursor:
            sql = "select id, name, physics, chemistry, maths, (physics+chemistry+maths) as total from marksheet where Physics>33 and Chemistry>33 and Maths>33 order by total desc limit 0,5"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.close()
            print("Id", '\t', "Name,"'\t', "Physics", '\t', "Chemistry", '\t', "Maths", )
            for d in result:
                print(d[0], '\t', d[1], '\t', d[2], '\t', d[3], '\t', d[4])

    def authenticate(self, id, name):
        result = " "
        connection = pymysql.connect(host="localhost", user="root", password="root", db="sunrays", port=3306)
        with connection.cursor() as cursor:
            sql = "select * from marksheet where id = (%s) and name = (%s)"
            data = (id, name)
            cursor.execute(sql, args=data)
            result = cursor.fetchall()
            if(not result):
                print("Invalid User")
            else:
                print("Verified.....")
                print("Id", '\t', "Name"'\t', "Physics", '\t', "Chemistry", '\t', "Maths" )
                for d in result:
                    print(d[0], '\t', d[1], '\t', d[2], '\t', d[3], '\t', d[4])
            connection.close()










