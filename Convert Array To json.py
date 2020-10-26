'''
in this program we basically don't use the dictionary
but we create a list and in this list we create a dictionary
'''
import json

a_list = []

a_list.append({
    "person" : "Sharlock Homles",
    "age" : 25,
    "sex":"male",
})

person_2 = dict()
person_2["person"]="Watson"
person_2["age"]=26
person_2["sex"]="male"

# add second person as a list in a list
a_list.append(person_2)

a_list.append({
    "person":"jim moritary",
    "age":22,
    "sex":"female"
})

# open a json file in write mode

file = open("ajsonfile.json","w")

# convert the list into json string

json_string = json.dumps(a_list,indent=4)

# now update the file with write lines

file.writelines(json_string)

file.close()

# easy way

direct_dump = json.dump(a_list,open('newfile.json','w'),indent=4)
