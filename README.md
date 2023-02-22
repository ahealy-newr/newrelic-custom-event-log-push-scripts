# newrelic-custom-event-log-push-scripts
### This repository contains scripts for pushing custom event and custom log data to New Relic's Telemetry Data Platform (TDP) using the Events and Logs API.

## PythonScripts

### Prerequisites
Before using these scripts, you will need to:
1. Have a New Relic account and New Relic API Licence key.
2. Have Python 3 installed on your system.

### CustomEvents
`py_event_push.py`: A Python script for pushing events to New Relic Insights using the Events API. <br>
`event_example_blob.json`: JSON file with example payload for event data

### CustomLogs
`py_log_push.py`: A Python script for pushing logs to New Relic's TDP using the Log API. <br>
`log_example_blob.json`: JSON file with example payload for log data

### Usage
Before running the scripts make sure to:
1. Update the licence.py file with your license key
2. For the py_push_event.py script, update the account id in the url value

To use the py_event_push.py and py_log_push.py script directly, simply run:

`python py_log_push.py`
`python py_event_push.py`

## License

This repository is licensed under the MIT License. See the LICENSE file for details.
