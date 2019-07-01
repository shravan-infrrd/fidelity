import glob
import os
from natsort import natsorted

def get_valid_data(text_file_path):
		text_files = natsorted(glob.glob(os.path.join(text_file_path, "*.txt")))
		for filename in text_files: #os.listdir(text_files):
				with open(filename) as fd:
						lines = fd.readlines()
						for line in lines:
								if "Exchange Traded Products" in line:
										return lines
		return []

def exchange_trade(text_file_path):
		etp = include_statement = False
		lines = get_valid_data(text_file_path)
		headers = ['Exchange Trade Products', 'Includes exchange-traded funds (ETFs), exchange-traded notes (ETNs), and other exchange-traded vehicles.']
		json_data = []
		if not lines:
				#json_data.append({"description":"Exchange Trade Products Not Found", "data": [], "headers": [], 'type': 'single'})
				json_data.append({"description": "Section Validation", "data": [False, False], "headers": headers, 'type': 'single'})
				return json_data
		
		etp = True
		found = False
		for line in lines:
				if "Includes exchange-traded funds".replace('-', ' ') in line.replace('-', ' '):
						include_statement = True
						found = True


		if found:
				#json_data.append({"description":"Includes exchange-traded funds - Statement Found", "data": [], "headers": [], 'type': 'single'})
				json_data.append({"description":"", "data": [ etp, include_statement ], "headers": headers, 'type': 'single'})
		else:
				#json_data.append({"description":"Includes exchange-traded funds - Statement Not Found", "data": [], "headers": [], 'type': 'single'})
				json_data.append({"description":"", "data": [ etp, include_statement ], "headers": headers, 'type': 'single'})

		return json_data
				
