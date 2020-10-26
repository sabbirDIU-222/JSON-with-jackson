'''
this time we don't make any file
but we make a json string and further also we make a new things that need to be updated with the json string
lets make a  json string
'''
import json

a_json_string = '''
            {
                 "name":"shimul islam sabbir",
                 "institute" : "daffodil international university",
                 "age":24,
                 "sex":"naked",
                 "room date":true
            }'''

# a python object to be appended

y = {"phone number":18212122}

# parse the string to dict

a_dictionary = json.loads(a_json_string)

a_dictionary.update(y)

print(a_dictionary)