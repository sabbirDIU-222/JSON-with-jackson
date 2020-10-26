'''
in this program we import requests module to download the json api data
and we get the data and make the data ad text format so that we can use the
loads function
'''
import json
import requests

request = requests.get("https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=ZtxzPXb5e-XWGTs6qTJz")

request_text = request.text

data = json.loads(request_text)
print(type(data))
# we convert the data into json again and store it into a file

data_serialization = json.dump(data,open("data.json","w"),indent=4)


# next target is how to add the data 
