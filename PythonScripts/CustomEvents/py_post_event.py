import requests
import json
import sys
sys.path.insert(1, '../../')
from PythonScripts.license import license_key

# Opening JSON file
f = open('event_example_blob.json')
event_data = json.load(f)
print(event_data)
# Closing file
f.close()

# Note: Change this if you're using an EU account.
use_eu_endpoint = False
# Note: You will need to your replace the XXXX with your New Relic Account Id
account_id = 'XXXX'

# Event API endpoints.
us_endpoint = f'https://insights-collector.newrelic.com/v1/accounts/{account_id}/events'
eu_endpoint = f'https://insights-collector.eu01.nr-data.net/v1/accounts/{account_id}/events'

endpoint = us_endpoint
if use_eu_endpoint:
  endpoint = eu_endpoint

headers = {'API-Key': f'{license_key}'}
response = requests.post(endpoint, headers=headers, json=event_data)
print(response)
