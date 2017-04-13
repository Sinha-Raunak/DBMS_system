from flask import Flask
from flaskext.mysql import MySQL
 
mysqlInstance = MySQL()
interface = Flask(__name__)
interface.config['MYSQL_DATABASE_USER'] = 'raunaksinha'
interface.config['MYSQL_DATABASE_PASSWORD'] = 'denim<3'
interface.config['MYSQL_DATABASE_DB'] = 'ques2'
interface.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysqlInstance.init_app(interface)
 
@interface.route("/")
def hello():
    return "App is just a variable "
 
if __name__ == "__main__":
    interface.run()
