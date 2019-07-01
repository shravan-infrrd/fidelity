import os
from constant import PROJECT_ROOT
import xmltodict
import json

def get_data():
		file_path = PROJECT_ROOT + "/temp_files/fidelity_2/page-23.txt"
		data = None
		with open(file_path) as fd:
				data = fd.readlines()

		return data

def get_footnote_file_data():
		file_path = PROJECT_ROOT + "/temp_files/fidelity_2"
		for filename in os.listdir(file_path):
				if 'txt' in filename:
						fn = file_path + '/' + filename
						with open(fn) as fd:
								lines = fd.readlines()
								for line in lines:
										if "positions held in cash account" in line:
												return lines


def only_footnotes():
		#lines = get_data()
		lines = get_footnote_file_data()
		footenotes = []
		for line in lines:
				split_data = line.split('  ')
				data = list( filter( None, split_data ) )

				try:
						if len(data[0]) == 1 or len(data[0]) == 2 or len(data[0]) == 3:
								footenotes.append(data[0])
				except:
						pass

		return footenotes

def get_footnotes():
		#lines = get_data()
		lines = get_footnote_file_data()
		footnotes = []
		for line in lines:
				split_data = line.split("  ")
				data = list( filter( None, split_data ) )
				#print(f"data--------->{data}")
				try:
						if len(data[0]) == 1 or len(data[0]) == 2 or len(data[0]) == 3:
								try:
										footenotes[-1][1] = description
								except:
										pass
								footnote = data[0]
								description = ""
								description = data[1]
								if len(footnote.strip()) > 0:
										#print(footnote)
										footnotes.append([ footnote, description ])
						else:
								try:
										#print("=========***=========", data[0].strip(), "=======1======", description)
										footnotes[-1][-1] = footnotes[-1][-1] + " " + data[0].strip()
								except:
										continue

				except:
						continue


		#print(f"footnotes----->{footnotes}")
	
		json_data = []
		json_data.append( {"description": "Footnote Extraction", "data": footnotes, "headers": ['Footnote', 'Description'], "type": 'multiple'} )

		return json_data



#footenotes = get_footnotes()

#data = get_footnote_file_data()
#print(data)	
