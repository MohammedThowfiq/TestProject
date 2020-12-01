import file_logic as m
import temp as t
import argparse

"""
Created on Mon Nov  30 13:15:40 2020

@author: MohammedThowfiq

"""

class datastore():
	
	def __init__(self, args):
		self.key = args.get('key', None)
		self.value = args.get('value', None)
		self.client = args.get('client', None)
		self.ttl = args.get('ttl', None)
		self.filepath = args.get('filepath', ".//")
		self.help = '''  
	1 for Create (--client --key  --ttl(optional) --value --filepath(optional)) 
	2 for Read (--client --key --filepath(optional)) 
	3 for Delete (--client --key --filepath(optional)) 
	4 for Reset (--client --filepath(optional))'''


	
	def create(self):
		if self.ttl:
			return m.create(self.client, self.key, self.value, ttl = int(self.ttl), filepath = self.filepath)
		else:
			return m.create(self.client, self.key, self.value, filepath = self.filepath)


	def read(self):
		return m.read(self.client, self.key, filepath = self.filepath)


	def delete(self):
		return m.delete(self.client, self.key, filepath = self.filepath)


	def reset(self):
		return m.reset(self.client, filepath = self.filepath)


def datastore_invoke(operation_name, **kwargs):

	operation = operation_name

	datastore_app = datastore(kwargs)
	
	status = ""

	if operation == 1:
		status = datastore_app.create()
	elif operation == 2:
		status = datastore_app.read()
	elif operation == 3:
		status = datastore_app.delete()
	elif operation == 4:
		status = datastore_app.reset()
	else:
		status = "Operation Not Found" + datastore_app.help

	return status


if __name__ == "__main__": 


	help =  '''  
	1 for Create (--client --key  --ttl(optional) --value --filepath(optional)) 
	2 for Read (--client --key --filepath(optional)) 
	3 for Delete (--client --key --filepath(optional)) 
	4 for Reset (--client --filepath(optional))'''


	parser = argparse.ArgumentParser()

	parser.add_argument("-k", "--key", help="Input Key")
	parser.add_argument("-v", "--value", help="Input Value")
	parser.add_argument("-c", "--client", help="client_file_name")
	parser.add_argument("-t", "--ttl", help="optional Time to live for Key(seconds)")
	parser.add_argument("-f", "--filepath", help="optional filepath ")
	parser.add_argument("-o", "--operation", help=help)


	args = parser.parse_args()
	client = args.client
	key = args.key
	value = args.value
	ttl = args.ttl
	filepath = args.filepath

	operation = int(args.operation)

	print(datastore_invoke(operation, client = client, key = key, value = value, ttl = ttl, filepath = filepath))

