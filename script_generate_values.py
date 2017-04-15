
from random import randint,choice
ins=["INSERT INTO "," VALUES(",")"]
tables=["Cargo","Facility_Type","Manufacturer","Rating","Shipment_Details","Transporter","Truck"]

CatCargo=["'Electric'","'Health'","'Medicine'","'Home'","'Sports'","'Cars'"]
Manufacturer=["'Reckitt'","'USHA'","'Apollo International'","'Maruti Suzuki'","'Auto Ignition'","'Indo Autotech'"]
Packaging=["'Pallet'","'Wooden Box'","'Finished Vehicle'","'Soft Wool'"]

FType=["'Factory'","'Warehouse'"]
FLocation=["'Sitarganj', 49","'Bilaspur', 51","'Mohan Coop.', 48","'Okhla', 47","'Manesar', 61","'Greater Noida', 68","'Palwal', 48" ,"'Faridabad', 27","'Gurgaon', 62","'Ballabgarh', 21"]
Tracking=["'No'","'Yes'"]
Loading=["'Manual'","'Forklift'","'Drive In'","'Trolley'"]
Transporter=["'Varuna Integrated'","'Om Logistics'","'DTDC'","'Majha Transport Pvt. Ltd.'","'TCI XPS'","'VRL Logistics'","'Associated Road Carriers'","'Shree Balaji Roadlines'","'Delhi Jaipur Transport'"]

TruckType=["22,15","22,9","24,15","24,20","32,15","32,16","32,20","34,24","40,27","40,32"]



numValues=50 # Change for different number of queries



for x in tables:
	for i in range(numValues):
		main=ins[0]+x+ins[1]
		# print "what"
		if x is "Cargo":
			main+=choice(CatCargo)+","+str(randint(30,90))+","+str(randint(1,10))+","+choice(Manufacturer)+","+choice(Packaging)
		elif x is "Facility_Type":
			main+=choice(FType)+","+choice(FLocation)+","+choice(Manufacturer)
		elif x is "Manufacturer":
			main+=choice(Manufacturer)+",Truck,"+choice(Tracking)+","+choice(Loading)+","+str(randint(1,9))+","+choice(Packaging)
		elif x is "Rating":
			main+=str(randint(1,5))+","+choice(Transporter)+","+choice(Manufacturer)
		elif x is "Shipment_Details":
			main+=choice(Transporter)+","+str(randint(30,90))+","+str(randint(15,50))+","+choice(Loading)+","+choice(CatCargo)+","+str(randint(150,500))
		elif x is "Transporter":
			main+=choice(Transporter)+","+str(randint(1,5))+","+str(randint(1,5))+","+str(randint(1,5))
		elif x is "Truck":
			main+=choice(Manufacturer)+","+choice(TruckType)+","+str(randint(40000,200000))
		main+=ins[2]
		print main