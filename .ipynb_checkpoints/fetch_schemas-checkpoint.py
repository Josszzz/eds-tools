""" 
Get the schemas from the EDS and put them in the schemas directory

JD 23/01/26
"""
import os
import requests
from urllib.parse import urljoin
import getpass
from pydantic import BaseModel
from eds_tools import get_token
from eds_routes import .


OUTPUT_DIR = './schemas'

def main():
    """ Get the schemas from the URLS, save to file """
    # Get an Auth token
    token = get_token()
    headers = {
        'Authorization': f'Bearer: {token}'
    }
    
    for schema_name, url in SCHEMA_URLS.items():
        try:
            resp = requests.get(urljoin(BASE_URL, url))
            resp.raise_for_status()
    
            with open(os.path.join(OUTPUT_DIR, f'{schema_name}.json'), 'w') as f:
                f.write(resp.text)
        except requests.exceptions.HTTPError as e:
            print(f'Could not get schema {schema_name} - {e}')
            

if __name__ == '__main__':
    main()