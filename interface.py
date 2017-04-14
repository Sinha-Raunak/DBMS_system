from flask import Flask
from flask import render_template
from flask import request
from flaskext.mysql import MySQL
#from flask.ext.appbuilder import Model

mysqlInstance = MySQL()
interface = Flask(__name__)
interface.config['MYSQL_DATABASE_USER'] = 'raunaksinha'
interface.config['MYSQL_DATABASE_PASSWORD'] = 'denim<3'
interface.config['MYSQL_DATABASE_DB'] = 'ques2'
interface.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysqlInstance.init_app(interface)
 
@interface.route("/") #This is the main function of intrerface app
def form_for_query_type(): #First Form
    return render_template("firstForm.html")
    
if __name__ == "__main__":
    interface.run()

@interface.route('/A',methods=['POST'])
def handler_first_form():
    print("reached Here")
    text = request.form.get('t')
    cursor = mysqlInstance.connect().cursor()
    cursor.execute(" select distinct dname from driver NATURAL JOIN cars NATURAL JOIN reserves where cname = %s",text)
    data = cursor.fetchall()
    print(data)
    
    #print(data)
    #print("THIS IS TEXT" + text)
    return str(data)

@interface.route("/Authenticate")
def Authenticate():
        #username = request.args.get('UserName')
        #password = request.args.get('Password')
        cursor = mysqlInstance.connect().cursor()
        cursor.execute(" select distinct dname from driver NATURAL JOIN cars NATURAL JOIN reserves where cname = 'Skoda'")
        data = cursor.fetchall()
        if data is None:
            return "Username or Password is wrong"
        else:
            print(data)
            return str(data)

