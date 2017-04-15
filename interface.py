from flask import Flask
from flask import render_template
from flask import request
from flaskext.mysql import MySQL
#from flask.ext.appbuilder import Model

mysqlInstance = MySQL()
interface = Flask(__name__)
interface.config['MYSQL_DATABASE_USER'] = 'root'
interface.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
interface.config['MYSQL_DATABASE_DB'] = 'DBMS_Project'
interface.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysqlInstance.init_app(interface)
 
@interface.route("/") #This is the main function of intrerface app
def form_for_query_type(): #First Form
    return render_template("firstForm.html")
    
if __name__ == "__main__":
    interface.run()


@interface.route('/AfterFirstSelection',methods=['POST'])
def handler_first_form():
    print("reached Here")
    input_first_form = request.form.get('SelectQuery')
    input_first_form = str(input_first_form)
    #database_search = mysqlInstance.connect().cursor()
    #based upon QuerySelect Have to decide query
    query_select = int(input_first_form)
    #QuerySelect.execute(" select distinct *  from Manufacturer where idManufacturer = %s",text)
    #data = cursor.fetchall()
    if query_select is 1:
	return render_template("Query1.html")
    elif query_select is 2:
	return render_template("Query2.html")
    elif query_select is 3:
	return render_template("Query3.html")
    elif query_select is 4:
	return render_template("Query4.html")
    elif query_select is 5:
	return render_template("Query5.html")
    elif query_select is 6:
	return render_template("Query6.html")
    elif query_select is 7:
	return render_template("Query7.html")
    elif query_select is 8:
	return render_template("Query8.html")
    elif query_select is 9:
	return render_template("Query9.html")
    return render_template("Query0.html")

@interface.route("/QueryProcessing",methods=['POST'])
def hadler_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer from Manufacturer NATURAL JOIN Facility_Type where location = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query0.html",output_tuple = data)


@interface.route("/QueryProcessing1",methods=['POST'])
def hadler_first_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query1.html",output_tuple = data)

@interface.route("/QueryProcessing2",methods=['POST'])
def hadler_second_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query2.html",output_tuple = data)

@interface.route("/QueryProcessing3",methods=['POST'])
def hadler_third_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query3.html",output_tuple = data)

@interface.route("/QueryProcessing4",methods=['POST'])
def hadler_fourth_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query4.html",output_tuple = data)

@interface.route("/QueryProcessing5",methods=['POST'])
def hadler_fifth_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query5.html",output_tuple = data)

@interface.route("/QueryProcessing6",methods=['POST'])
def hadler_sixth_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query6.html",output_tuple = data)

@interface.route("/QueryProcessing7",methods=['POST'])
def hadler_seventh_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query7.html",output_tuple = data)

@interface.route("/QueryProcessing8",methods=['POST'])
def hadler_eight_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query8.html",output_tuple = data)

@interface.route("/QueryProcessing9",methods=['POST'])
def hadler_ninth_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query9.html",output_tuple = data)

@interface.route("/QueryProcessing10",methods=['POST'])
def hadler_thenth_query():
	if request.method == 'POST':
		output_form = request.form.get('X')
    		database_search = mysqlInstance.connect().cursor()
    		database_search.execute(" select idManufacturer,Packaging  from Manufacturer where Tracking = %s",output_form)
   		data = database_search.fetchall()
		print(data)
		return render_template("Query10.html",output_tuple = data)


