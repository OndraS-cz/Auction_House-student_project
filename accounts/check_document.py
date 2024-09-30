import requests
from django.core.exceptions import ValidationError


MVCR_URL = 'https://aplikace.mvcr.cz/neplatne-doklady/doklady.aspx'

def check_document(document_number, document_type):
    result = None
    params = {'dotaz': document_number, 'doklad': document_type}
    response = requests.get(MVCR_URL, params=params)
    if response.status_code == 200:
        if 'evidovano="ano"/' in response.text.lower():
            raise ValidationError('Doklad totožnosti byl nalezen v databázi neplatných dokladů!')
        else:
            result = True  # 'Doklad je platný nebo nebyl nalezen.'
    else:
        result = False  # 'Chyba při ověřování dokladu.'
    print(result)
    return result