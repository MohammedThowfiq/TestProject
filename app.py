import file_logic as m
import temp as t
from time import sleep
import threading

"""
Created on Tue Dec  30 13:15:40 2020

@author: MohammedThowfiq

"""


class test:
	client = "Thowfiq"
	key = "test"
	key_int = 10
	key_more_than_32 = "World is in danger so takecare"
	value_dict = {"Registered_firm" : 
	{ 
   "firm":"Strictly Android Apps",
   "location":"chennai",
   "products":{ 
      "Product-1":"COVIZER",
      "Product-2":"Vehicle Recognition",
      "Product-3":"FIR Management System"
   }
   }
   }
	value_json_type = { "employee":"Mohammed", "status":"fresher", "role":"App Developer" }
	value_string = "Steve Rogers"
	ttl_value = 10


def create(s):
	print(m.create(s.client, s.key, s.value_json_type)+"\n")			
	print(m.create(s.client, s.key_int, s.value_json_type)+"\n")		
	print(m.create(s.client, s.key, s.value_dict)+"\n")				
	print(m.create(s.client, s.key_more_than_32, s.value_json_type)+"\n")
	print(m.create("FedEX", s.key_int, s.value_dict)+"\n")				
	print(m.create(s.client, "Employer", s.value_string)+"\n")			
	print(m.create(s.client, "Executive", s.value_dict, ttl = s.ttl_value)+"\n")


def read(s):
	print(m.read(s.client, s.key)+"\n")									
	print(m.read(s.client, s.key_int)+"\n")								
	print(m.read("Sanmania", s.key)+"\n")										
	print(m.read(s.client, "Executive")+"\n")								
	print("\nSleeping mode...\n")
	sleep(31)
	print(m.read(s.client, "Executive")+"\n")								


def delete(s):
	print(m.delete(s.client, s.key)+"\n")									
	print(m.delete(s.client, s.key_more_than_32)+"\n")					
	print(m.delete("Temenos", s.key)+"\n")									
	print(m.delete(s.client, "Executive")+"\n")								


def create_2(s):
	print(m.create("sherlock", s.key, s.value_json_type)+"\n")


def append_2(s):
	print(m.create("sherlock", s.key, s.value_dict)+"\n")
	print(m.delete("sherlock", s.key)+"\n")


def unit_begin(s):
	
	print( "\n\n--------------- Create mode  ---------------\n\n")
	create(s)
	print( "\n\n--------------- Read mode  ---------------\n\n")
	read(s)
	print( "\n\n--------------- Delete mode  ---------------\n\n")
	delete(s)
	print( "\n\n--------------- Reset mode  ---------------\n\n")
	print(m.reset(s.client))

if __name__ == "__main__": 
    
    print("\n---------------General Test ---------------\n")
    obj = test()
    unit_begin(obj)

    print("\n--------------- Thread-Safe Code Test ---------------\n")
   
    t1 = threading.Thread(target=create_2, args=(obj,)) 
    t2 = threading.Thread(target=append_2, args=(obj,)) 
  
    t1.start() 
    t2.start() 
   
    t1.join() 
    t2.join() 
  
    print("Thread-safe Testing done")
