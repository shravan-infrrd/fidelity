from constant import PROJECT_ROOT

from lib.fidelity.read_xml_file import xml_total_common_stock, xml_total_preferred_stock, xml_total_stocks

def get_data():
		text_file = PROJECT_ROOT + "/temp_files/fidelity_2/page-17.txt"
		with open( text_file ) as fp:
				contents = fp.readlines()

		return contents

def total_common_stock():
		lines = get_data()
		val = None
		for line in lines:
				if "Total Common Stock" in line:
						words = line.split('  ')
						valid_words = list( filter( None, words ) )
						bb_val = float(valid_words[2].replace('$', '').replace(',',''))
						val = float(valid_words[1].replace('$', '').replace(',',''))
						ey = float(valid_words[3].strip().replace('$', '').replace(',',''))
						break

		xml_data = xml_total_common_stock()
		data = [ val, xml_data[0], (val == float(xml_data[0])), bb_val, xml_data[1], (bb_val == float(xml_data[1])), ey, xml_data[2], (ey == float(xml_data[2]))  ]
		headers = ["PDF Beginning Value", "XML BB Value", "BB Validation", "PDF Ending Value", "XML END Value", "END Validation", "PDF EY", "XML EY Value", "EY Validation" ]


		json_data = []
		json_data.append( {"description": "Common Stock", "data": data , "headers": headers, "type": 'single'} )


		print(f"JSON_DATA------>{json_data}")

		return json_data


def total_preferred_stock():
		lines = get_data()
		val = None
		for line in lines:
				if "Total Preferred Stock" in line:
						words = line.split('  ')
						valid_words = list( filter( None, words ) )

						print(f"valid_words--->{valid_words}")
						bb_val = float(valid_words[2].replace('$', '').replace(',',''))
						val = float(valid_words[1].replace('$', '').replace(',',''))
						try:
								ey = float(valid_words[3].strip().replace('$', '').replace(',',''))
						except:
								ey = 0
						break

		xml_data = xml_total_preferred_stock()
		data = [ val, xml_data[0], (val == float(xml_data[0])), bb_val, xml_data[1], (bb_val == float(xml_data[1])), ey, xml_data[2], (ey == float(xml_data[2]))  ]
		headers = ["PDF Beginning Value", "XML BB Value", "BB Validation", "PDF Ending Value", "XML END Value", "END Validation", "PDF EY", "XML EY Value", "EY Validation" ]

		json_data = []
		json_data.append( {"description": "Preferred Stock", "data": data, "headers": headers, "type": "single"} )
		return json_data

def total_stock():
		lines = get_data()
		val = None
		for line in lines:
				if "Total Stocks" in line:
						words = line.split('  ')
						valid_words = list( filter( None, words ) )
						bb_val = float(valid_words[2].replace('$', '').replace(',',''))
						val = float(valid_words[1].replace('$', '').replace(',',''))
						ey = float(valid_words[3].strip().replace('$', '').replace(',',''))
						break

		xml_data = xml_total_stocks()
		data = [ val, xml_data[0], (val == float(xml_data[0])), bb_val, xml_data[1], (bb_val == float(xml_data[1])), ey, xml_data[2], (ey == float(xml_data[2]))  ]
		headers = ["PDF Beginning Value", "XML BB Value", "BB Validation", "PDF Ending Value", "XML END Value", "END Validation", "PDF EY", "XML EY Value", "EY Validation" ]

		json_data = []
		json_data.append( {"description": "Total Stock", "data": data, "headers": headers, "type": "single"} )
		return json_data


