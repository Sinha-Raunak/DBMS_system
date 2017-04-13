from flask import Flask,request
from flaskext.mysql import MySQL
 
mysqlInstance = MySQL()
interface = Flask(__name__)
interface.config['MYSQL_DATABASE_USER'] = 'raunaksinha'
interface.config['MYSQL_DATABASE_PASSWORD'] = 'denim<3'
interface.config['MYSQL_DATABASE_DB'] = 'ques2'
interface.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysqlInstance.init_app(interface)
 
@interface.route("/") #This is the main function of intrerface app
def hello():
    return "App is just a variable "
 
if __name__ == "__main__":
    interface.run()

@interface.route("/Authenticate")
def Authenticate():
        #username = request.args.get('UserName')
        #password = request.args.get('Password')
        cursor = mysqlInstance.connect().cursor()
        cursor.execute("SELECT * from cars where cid = '20001' ")
        data = cursor.fetchone()
        if data is None:
            return "Username or Password is wrong"
        else:
            print(data)
            return "HAHAHA"

