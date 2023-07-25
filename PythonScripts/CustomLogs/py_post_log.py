import requests
import json
import sys
sys.path.insert(1, '../../')
from PythonScripts.conf import license_key, datacentre

#log_msg = "log message"
# Opening JSON file
f = open('log_example_blob.json')
log_msg = json.load(f)
print(log_msg)
# Closing file
f.close()

# Log API endpoints.
if datacentre == 'us':
  endpoint = f'https://log-api.newrelic.com/log/v1'
else:
  endpoint = f'https://log-api.eu.newrelic.com/log/v1'

headers = {'API-Key': f'{license_key}'}
response = requests.post(endpoint, headers=headers, json=log_msg)
print(response)