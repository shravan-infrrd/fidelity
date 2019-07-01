import glob
import os
from natsort import natsorted
from constant import PROJECT_ROOT
import re
from lib.generic.identify_footnote import only_footnotes
from lib.generic.read_xml_file import get_stocks_data

def extract_foot_note(footnotes, description):
		footnote = description.split(' ')[0]
		if len(footnote) > 2:
				return ['NA', '-']
		if footnote:
				valid_footnote = footnote in footnotes
				return [footnote, valid_footnote]
		else:
				return ['NA', '-']


def append_total_cost_basis(data, xml_file):
		stocks = get_stocks_data( xml_file )
		flag = False
		for i, d in enumerate(data):
				
				try:
						if float(stocks[i][6]) > 0.0:
								flag = True
				except:
						flag = False
				d.append(stocks[i][7])
				d.append(stocks[i][6])
				d.append(stocks[i][5])
				
		if flag:
				return [True, data]
		else:
				return [False, data]


def identify_stocks_file( contents ):
		#print("*******identify_stocks_file*********", contents)
		holdings = stocks = common_stock = False
		#print("*******START of LOOP*******")
		for content in contents:
				#print(f"content-->{content}")	
				if 'Holdings' in content:
						holdings = True
				if 'Stocks' in content:
						stocks = True
				if 'Common Stock' in content:
						common_stock = True

		if holdings and stocks and common_stock:
				return True
		else:
				return False

def extract_cs( text_file_path="", xml_file=""):
		data = []
		footnotes = only_footnotes(text_file_path)
		pdf_flag_for_tota_cost_basis = False
		text_files = natsorted(glob.glob(os.path.join(text_file_path, "*.txt")))
		note = ""
		print(f"text_files----->{text_files}")
		#for filename in os.listdir(text_file_path):
		for filename in text_files:
				#text_file = text_file_path + "/" + filename
				text_file = filename
				contents = None
				#print(f"Text File--->{text_file}")
				with open(text_file) as fd:
						contents = fd.readlines()
				#print(identify_stocks_file( contents ))
				if identify_stocks_file( contents ):
						flag = False
						page = []
						for content in contents:
								if 'Preferred Stock' in content:
										break
								if 'Common Stock' in content:
										flag = True
										continue
								else:
										if not flag:
												continue
								
								
								if flag:
										words = content.strip().split('  ')
										raw_values = list( filter( None, words ) )
										values = []
										for rv in raw_values:
												values.append(rv.strip())
																		
										if values:
												#print(f"data---->{data}")
												if len(values) == 1:
														if not re.findall(r"\d+ of \d+", values[0]):
																if page:
																		page[-1][0] = page[-1][0] + " " + values[0]
												else:
														if len(values) >= 5:
																page.append(values)
																if len(values) == 7:
																		values.pop()
																		#data.append(values)
																elif len(values) == 5:
																		values.append("")
																		#data.append(values)
            
            
																if len(values) <= 6:
																		pdf_flag_for_tota_cost_basis = True
																#elif len(values) == 6:
																		#data.append(values)
															
																values.extend( extract_foot_note(footnotes, values[0])  )
																data.append(values)
            
				flag = False
		total_cost_basis, data = append_total_cost_basis(data, xml_file)
		if total_cost_basis and pdf_flag_for_tota_cost_basis:
				note = "Missing Column: Total Cost Basis"
		json_data = []

		if note:
				json_data.append({"description": "Common Stocks", "note": note, "data": data, 'type': 'multiple', 'headers': ['Description', 'Beginning Market Value Mar 20, 2019', 'Quantity Mar 21, 2019', 'Price Per Unit Mar 21, 2019', 'Ending Market Value Mar 21, 2019', 'EAI (S$)/ EY (%)', 'Footnote', 'Footnote Validation', 'XML Footnote', 'Total Cost Basis', 'BB-Mkt-Val']} )
		else:
				json_data.append({"description": "Common Stocks", "data": data, 'type': 'multiple', 'headers': ['Description', 'Beginning Market Value Mar 20, 2019', 'Quantity Mar 21, 2019', 'Price Per Unit Mar 21, 2019', 'Ending Market Value Mar 21, 2019', 'EAI (S$)/ EY (%)', 'Footnote', 'Footnote Validation', 'XML Footnote', 'Total Cost Basis', 'BB-Mkt-Val']} )
		return json_data

def extract_ps( text_file_path="", xml_file=""):
		data = []
		footnotes = only_footnotes(text_file_path)
		pdf_flag_for_tota_cost_basis = False
		text_files = natsorted(glob.glob(os.path.join(text_file_path, "*.txt"))) 
		#for filename in os.listdir(text_file_path):
		for filename in text_files:
				#text_file = text_file_path + "/" + filename
				text_file = filename
				contents = None
				print(f"Text File--->{text_file}")
				with open(text_file) as fd:
						contents = fd.readlines()

				if identify_stocks_file( contents ):
						flag = False
						page = []
						for content in contents:
								if 'Bonds' in content:
										break
								if 'Preferred Stock' in content:
										flag = True
										continue
								else:
										if not flag:
												continue
								
								
								if flag:
										words = content.strip().split('  ')
										raw_values = list( filter( None, words ) )
										values = []
										for rv in raw_values:
												values.append(rv.strip())
																		
										if values:
												#print(f"data---->{data}")
												if len(values) == 1:
														if not re.findall(r"\d+ of \d+", values[0]):
																if page:
																		page[-1][0] = page[-1][0] + " " + values[0]
												else:
														if len(values) >= 5:
																page.append(values)
																if len(values) == 7:
																		values.pop()
																		#data.append(values)
																elif len(values) == 5:
																		values.append("")
																		#data.append(values)
            
            
																if len(values) <= 6:
																		pdf_flag_for_tota_cost_basis = True
																#elif len(values) == 6:
																		#data.append(values)
															
																values.extend( extract_foot_note(footnotes, values[0])  )
																data.append(values)
            
				flag = False

		json_data = []
		note = "hello"
		json_data.append({"description": "Preferred Stocks", "data": data, 'type': 'multiple', 'headers': ['Description', 'Beginning Market Value Mar 20, 2019', 'Quantity Mar 21, 2019', 'Price Per Unit Mar 21, 2019', 'Ending Market Value Mar 21, 2019', 'EAI (S$)/ EY (%)']} )
		return json_data

