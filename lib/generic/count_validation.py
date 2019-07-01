
from lib.generic.stocks import extract_cs, extract_ps
from lib.generic.read_xml_file import get_stocks_data, get_preferred_stocks_data



def stock_ev(text_file_path, xml_file):

    pdf_count_data = len(extract_cs( text_file_path, xml_file)[0]['data'])
    xml_count_data = len(get_stocks_data(xml_file))

    data = [ pdf_count_data, xml_count_data, (pdf_count_data == xml_count_data) ]
    json_data = []
    json_data.append( {"description": "Stock Extraction Validation", "data": data, "headers": ["PDF Extraction Count", "XML Validation Count", "Result"], "type": 'single'})
    return json_data


def preferred_stock_ev(text_file_path, xml_file):

    pdf_count_data = len(extract_ps( text_file_path, xml_file)[0]['data'])
    xml_count_data = len(get_preferred_stocks_data( xml_file))

    data = [ pdf_count_data, xml_count_data, (pdf_count_data == xml_count_data) ]
    json_data = []
    json_data.append( {"description": "Stock Extraction Validation", "data": data, "headers": ["PDF Extraction Count", "XML Validation Count", "Result"], "type": 'single'})
    return json_data


