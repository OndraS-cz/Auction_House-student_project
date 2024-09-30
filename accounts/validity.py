import requests
import xml.etree.ElementTree as ET

url = 'https://aplikace.mvcr.cz/neplatne-doklady/doklady.aspx?dotaz=123456AB&doklad=0'

def fetch_invalid_documents(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('invalid_documents.xml', 'wb') as f:
            f.write(response.content)
    else:
        print(f'Failed to fetch data. Status code: {response.status_code}')

fetch_invalid_documents(url)

def parse_invalid_documents(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    invalid_docs = []
    for record in root.findall('.//Record'):
        doc_number = record.find('docNumber').text
        doc_type = record.find('docType').text
        invalid_docs.append({
            'number': doc_number,
            'type': doc_type,
        })
    return invalid_docs

invalid_documents = parse_invalid_documents('invalid_documents.xml')
