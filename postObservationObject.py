__author__ = 'sasaki'
import http.client

import config


httpConnection = http.client.HTTPConnection(host=config.host, port=config.port)
httpConnection.request("POST", "/" + config.dbname, '{"test":1}', headers={"Content-type": "application/json"})
response = httpConnection.getresponse()
print(response.status, response.reason, response.readall())
