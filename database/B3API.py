import json
import requests
import pandas as pd

def get_b3_data(derivatives=None):
    """
    derivate data from the B3 API.

    Args:
        derivatives (list[str], optional):
            Defaults to ["DI1", "FRC", "DAP"].

    Returns:
        list[dict]: List of JSON responses from the B3 API.
    """

    data = []  
    if derivatives is None:
        derivatives = ["DI1", "FRC", "DAP"]
    
    for each in derivatives:

        url = "https://cotacao.b3.com.br/mds/api/v1/DerivativeQuotation/" + each

        try:
            rqts = requests.get(url, timeout=10)
            
        except requests.exceptions.RequestException as e:
            print("Error in request: ", e)
            exit()

        try:
            text = rqts.text
            json_rqts = json.loads(text)
           
        except json.JSONDecodeError as e:
            print("Error decoding JSON: ", e)
            exit()

        data.append(json_rqts)

    with open("database\\DerivativesQuotation.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return print('[SUCCESS] Data fetched from B3 API and saved to DerivativesQuotation.json')