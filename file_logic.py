import temp as t
import logging
import threading
import json  

"""
Created on Tue Dec  30 13:15:40 2020

@author: MohammedThowfiq

"""

logging.basicConfig(filename='datastore_app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

lock = threading.RLock()

def create(client, key, value, **kwargs):
	ttl_value = kwargs.get('ttl', None)
	
	filepath = kwargs.get('filepath', ".//")
	with lock:
		if isinstance(value, str):
			try:
				value = json.loads(value)
			except:
				value = value
		
		status = t.create_operation(client, key, value, filepath = filepath , ttl = ttl_value)
		
		if 'successfull' in status:
			return "Create Operation Done"
		elif 'denied' in status:
			logging.error(status)
			return "Error occurred while creating : " + status
		else:
			logging.error(status)
			return "Error Status : " + status


def delete(client, key, **kwargs):
	filepath = kwargs.get('filepath', ".//")
	with lock:
		status = t.delete_operation(client, key, filepath = filepath)
		if 'Deleted' in status:
			return status
		elif 'not found' in status:
			logging.error(status)
			return status
		else:
			logging.error(status)
			return "Error Status : " + status


def read(client, key, **kwargs):
	filepath = kwargs.get('filepath', ".//")
	with lock:
		status = t.read_operation(client, key, filepath = filepath)
		if 'not found' in status:
			logging.error(status)
			return status
		elif 'value' in status:
			return status
		else:
			logging.error(status)
			return "Error Status : " + status


def reset(client, **kwargs):
	filepath = kwargs.get('filepath', "")
	with lock:
		status = t.reset_operation(client, filepath = filepath)
		logging.info(status)
		return status

