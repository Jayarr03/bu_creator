import requests
import json
import pandas as pd
import config

baseURL = "https://james-rabe.iriusrisk.com//api/v1/"

business_unit_endpoint = f"{baseURL}businessunits"

def bu_creator(bu_ref,bu_name,bu_desc):
    payload = json.dumps({
        "ref": f"{bu_ref}",
        "name": f"{bu_name}",
        "desc": f"{bu_desc}"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'api-token': config.API_KEY
    }

    response = requests.request("POST", business_unit_endpoint, headers=headers, data=payload)

    #print(response.text)
    if response.status_code == 201:
        print(f"Status code 201: {bu_name} was added successfully!")
    else:
        print(f"Status code {response.status_code}: {bu_name} was not added!")

#sheet_name = "Sheet1"  # Replace "Sheet1" with the actual sheet name you want to read

data = pd.read_csv(r'C:\Users\jrabe_iriusrisk\PycharmProjects\bu_creator\bu_mappings.csv')  # Replace 'your_spreadsheet.csv' with the actual file name and path

counter = 1

for index, row in data.iterrows():

  counter += 1

  #create a spreadsheet with column headers and match those the variables in this script.

  bu_name = str(row['business_unit_name'])
  bu_ref = str(row['business_unit_refID'])
  bu_desc = str(row['description'])

  bu_creator(bu_ref,bu_name,bu_desc)
