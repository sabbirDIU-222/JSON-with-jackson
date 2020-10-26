'''
javascript object notation
firstly we learn about the jason string to python dictionary
and convert it dictionary to json string
loads and dumps method will help us
'''
import json

json_string = '''
             {
               "person quality":{"education":"bsc ssc hsc",
                                  "expert" : "expert in android and xml and data analysis",
                                  "taking" :  false
                                  },
                "system management" : null,
                "love":true,
                "age":22
                
             }'''

python_dictionary = json.loads(json_string)
'''for i in python_dictionary['person quality']:
    print(i)'''
'''print(type(python_dictionary))'''

print(python_dictionary)

# python dictionary to json string

json_str = json.dumps(python_dictionary,indent=4)
print(json_str)

# or we can make  a new dictionary
a_new_dictionary = {

    "name":"ali baba",
    "sex" : "male",
    "education":["cbshm","cpscm","diu","bma","dsc","dr","california"],
    "married" : False,
    "love":True,
    "age":45,

}

a_new_json_string = json.dumps(a_new_dictionary,indent=4)
print(a_new_json_string)