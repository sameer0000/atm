import pymysql
class Validate:
    def adduser(self,user):
        sql = "insert into user values('"+user.getusername()+"','"+user.getpassword()+"')"
        print sql
        db = pymysql.connect("localhost","root","swecha","userexp" )
        cursor = db.cursor()
        cursor.execute(sql)
        db.close()