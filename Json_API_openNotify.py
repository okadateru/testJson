# -*- coding: utf-8 -*-

import json
import requests

# import pymysql, os

# response = requests.get("http://api.open-notify.org/iss-pass")
#print(response.status_code)

parameters = {"lat": 40.71, "lon": -74}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# Print the content of the response (the data the server returned)
print(response.content)
# This gets the same data as the command aboveresponse = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")

#
# try:
# 	json_data = json.loads(response, object_pairs_hook=OrderedDict)
# except JSONDecodeError:
# 	logger.exception('Error when parsing JSON, raw data was ' + str(raw_data))
# 	raise ExternalAPIException('Unable to do my work! Invalid JSON data returned.')