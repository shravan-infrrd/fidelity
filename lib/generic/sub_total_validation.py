import os
from constant import PROJECT_ROOT

from lib.generic.read_xml_file import xml_total_cs, xml_total_ps, xml_ts

def get_data(text_file_path, keyword):
		for filename in os.listdir(text_file_path):
				if 'txt' in filename:
						fn = text_file_path + '/' + filename
						with open(fn) as fd:
								lines = fd.readlines()
								for line in lines:
										if keyword in line:
												return lines

		return []
		"""
		text_file = PROJECT_ROOT + "/temp_files/fidelity_2/page-17.txt"
		with open( text_file ) as fp:
				contents = fp.readlines()

		return contents
		"""

def total_cs(text_file_path, xml_path):
		lines = get_data( text_file_path, "Total Common Stock" )
		val = None
		for line in lines:
				if "Total Common Stock" in line:
						words = line.split("  ")
						print(f"valid_words------>{words}")
						valid_words = list( filter( None, words ) )
						print(f"valid_words------>{valid_words}")
						bb_val = float(valid_words[2].replace('$', '').replace(',',''))
						val = float(valid_words[1].replace('$', '').replace(',',''))
						ey = float(valid_words[3].strip().replace('$', '').replace(',',''))
						break

		xml_data = xml_total_cs(xml_path)
		data = [ val, xml_data[0], (val == float(xml_data[0])), bb_val, xml_data[1], (bb_val == float(xml_data[1])), ey, xml_data[2], (ey == float(xml_data[2]))	]
		headers = ["PDF Beginning Market Value", "XML Beginning Market Value", "BB-MKT-Val Validation", "PDF Ending Market Value", "XML Ending Market Value", "END Validation", "PDF EY Value", "XML EY Value", "EY Validation" ]


		json_data = []
		json_data.append( {"description": "Common Stock", "data": data , "headers": headers, "type": 'single'} )


		print(f"JSON_DATA------>{json_data}")

		return json_data


def total_ps(text_file_path, xml_path) :
		lines = get_data( text_file_path, 'Total Preferred Stock')
		val = None
		val = bb_val = ey = 0.0
		for line in lines:
				if "Total Preferred Stock" in line:
						words = line.split("  ")
						valid_words = list( filter( None, words ) )

						print(f"valid_words--->{valid_words}")
						bb_val = float(valid_words[2].replace('$', '').replace(',',''))
						val = float(valid_words[1].replace('$', '').replace(',',''))
						try:
								ey = float(valid_words[3].strip().replace('$', '').replace(',',''))
						except:
								ey = 0
						break

		xml_data = xml_total_ps(xml_path)
		if xml_data:
				data = [ val, xml_data[0], (val == float(xml_data[0])), bb_val, xml_data[1], (bb_val == float(xml_data[1])), ey, xml_data[2], (ey == float(xml_data[2]))	]
		else:
				data = [0, 0, True, 0, 0, True,0, 0, True]
		#headers = ["PDF Beginning Value", "XML BB Value", "BB Validation", "PDF Ending Value", "XML END Value", "END Validation", "PDF EY", "XML EY Value", "EY Validation" ]
		headers = ["PDF Beginning Market Value", "XML Beginning Market Value", "BB-MKT-Val Validation", "PDF Ending Market Value", "XML Ending Market Value", "END Validation", "PDF EY Value", "XML EY Value", "EY Validation" ]

		json_data = []
		json_data.append( {"description": "Preferred Stock", "data": data, "headers": headers, "type": "single"} )
		return json_data

def total_s( text_file_path, xml_path ):
		lines = get_data(text_file_path, "Total Stocks")
		val = None
		val = bb_val = ey = 0.0
		for line in lines:
				if "Total Stocks" in line:
						words = line.split("  ")
						valid_words = list( filter( None, words ) )
						bb_val = float(valid_words[2].replace('$', '').replace(',',''))
						val = float(valid_words[1].replace('$', '').replace(',',''))
						ey = float(valid_words[3].strip().replace('$', '').replace(',',''))
						break

		xml_data = xml_ts(xml_path)
		data = [ val, xml_data[0], (val == float(xml_data[0])), bb_val, xml_data[1], (bb_val == float(xml_data[1])), ey, xml_data[2], (ey == float(xml_data[2]))	]
		#headers = ["PDF Beginning Value", "XML BB Value", "BB Validation", "PDF Ending Value", "XML END Value", "END Validation", "PDF EY", "XML EY Value", "EY Validation" ]
		headers = ["PDF Beginning Market Value", "XML Beginning Market Value", "BB-MKT-Val Validation", "PDF Ending Market Value", "XML Ending Market Value", "END Validation", "PDF EY Value", "XML EY Value", "EY Validation" ]

		json_data = []
		json_data.append( {"description": "Total Stock", "data": data, "headers": headers, "type": "single"} )
		return json_data


