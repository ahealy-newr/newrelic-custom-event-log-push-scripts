import requests
import json
import sys
sys.path.insert(1, '../../')
from PythonScripts.conf import license_key, datacentre, rpm_account_id

# Opening JSON file
f = open('event_example_blob.json')
event_data = json.load(f)
print(event_data)
# Closing file
f.close()

# Event API endpoints.
if datacentre == 'us':
  endpoint = f'https://insights-collector.newrelic.com/v1/accounts/{rpm_account_id}/events'
else:
  endpoint = f'https://insights-collector.eu01.nr-data.net/v1/accounts/{rpm_account_id}/events'

# Create headers and push event
headers = {'API-Key': f'{license_key}'}
response = requests.post(endpoint, headers=headers, json=event_data)
print(response)
