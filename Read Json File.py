'''
recently we created a json file and put some python dictionary to convert it as json dumps method
now we get access some item from this json file
'''
import json

# open file in read mood
file = open("ajsonfile.json","r")

# read data

content = file.read()

# convert the json string as python list
# remember this time also loads method called because we parse the data as a string formet in read
python_list = json.loads(content)

for data in python_list:
    name = data.get('person')
    age = data.get('age')
    sex = data.get('sex')

    print(f"the name is {name}  age is {age}  sex {sex}")


file.close()