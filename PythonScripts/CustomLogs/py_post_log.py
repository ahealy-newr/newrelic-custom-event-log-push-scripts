import requests
import json
import sys
sys.path.insert(1, '../../')
from PythonScripts.license import license_key

#log_msg = "log message"
# Opening JSON file
f = open('log_example_blob.json')
log_msg = json.load(f)
print(log_msg)
# Closing file
f.close()

# Log API endpoint 
us_endpoint = "https://log-api.newrelic.com/log/v1"
headers = {'API-Key': f'{license_key}'}
response = requests.post(us_endpoint, headers=headers, json=log_msg)
print(response)