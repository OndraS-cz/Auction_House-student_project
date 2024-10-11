import re

import requests
from django.core.exceptions import ValidationError


# kontrola přítomnosti dokladu totožnosti v databázi neplatných dokladů

MVCR_URL = 'https://aplikace.mvcr.cz/neplatne-doklady/doklady.aspx'

def check_document(document_number, document_type):
    result = None
    params = {'dotaz': document_number, 'doklad': document_type}
    response = requests.get(MVCR_URL, params=params)
    print(response.text)
    if response.status_code == 200:
        if re.search('evidovano="ano"', response.text.lower()):
            result = False
        else:
            result = True
    else:
        result = False
    print(result)
    return result