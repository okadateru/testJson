# -*- coding: utf-8 -*-

import json
import requests

parameters = {"lat": 40.71, "lon": -74}
headers = {"content-type": "application/json"}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters, headers=headers)

data = response.json()

print(json.dumps(data, indent=4))



# try:
# 	json_data = json.loads(response, object_pairs_hook=OrderedDict)
# except JSONDecodeError:
# 	logger.exception('Error when parsing JSON, raw data was ' + str(raw_data))
# 	raise ExternalAPIException('Unable to do my work! Invalid JSON data returned.')