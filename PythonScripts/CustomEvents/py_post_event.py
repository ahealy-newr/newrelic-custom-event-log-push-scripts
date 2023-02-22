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

# US Event API endpoint. Note: You will need to your replace the XXXX with your New Relic Account Id
us_endpoint = "https://insights-collector.newrelic.com/v1/accounts/XXXXX/events"
headers = {'API-Key': f'{license_key}'}
response = requests.post(us_endpoint, headers=headers, json=event_data)
print(response)