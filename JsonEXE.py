'''
json
1. json string
2. python dictionary
3. load ,loads
4. dump ,dumps
5. file handling json
6. requests module
7. quandal website data api json
'''
import json

json_string = '''
            {  
            
              "person":["mamun","sabbir","moti","sagor"],
              "education":{"education":"bsc ssc hsc",
                                  "expert" : "expert in android and xml and data analysis",
                                  "taking" :  false
                           },
              "sex":"male"
            
            }
'''

# data enterchange json string - > python dictionary -> loads()

python_dictionary = json.loads(json_string)

again_json_string = json.dumps(python_dictionary,indent=4,sort_keys=True)
print(again_json_string)


# python dictionary

mamun_info = {
    "Name" : " Mamun",
    "age" : 23,
    "sex" : "Male",
    "Married" : True,
    "skill":["java","python","c","algorithm","html","css","teaching"],
    "list of reading book":{
        "physics" : ["hsc","ssc"],
        "humaun" : "misir ali",
        "ahamed sofa":"joddopi amar guru",
        "jafor iqbal":"project  nabula"
   },
    "having fight" : None
}

# json string
# dumps

variable_json =json.dumps(mamun_info,indent=4)
#variable_dict = json.loads(variable_json)

'''file = open("mamuninfo.txt","w")

file.writelines(variable_dict)'''
file = json.dump(mamun_info,open("mamunjson.json","w"),indent=4)
print(type(file))

# load work
with open('ajsonfile.json') as a:
    data = json.load(a)

print(data)