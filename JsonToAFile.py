'''
1. we now create a dictionary and make convert it in json string formet
2. but we make it as an text file and make sure that we can write into it

'''
import json

python_dictionary = {
    "person":["sabbir","mamun","sinthia","lopa","mahin","sagor","robi","moti"],
    "sabbir":{
        "skill":["java","python","dart","c","android","data analysis","data view"],
        "age" : 23,
        "semester":6,
        "sex":True
    },
    "mamun":{
        "skill":["java","python","dart","c"],
        "age" : 23,
        "semester":6,
        "sex":True
    },
    "sinthia":{
        "skill":["java","python","dart","c","android","data analysis","data view"],
        "age" : 23,
        "semester":6,
        "sex":None
    },

}

with open("amderinfo.txt","w") as info:
    json.dump(python_dictionary,info,indent=4)

# in the main folder we will find a file named as amderinfo.txt

info.close()
'''a_new_dict = {
    "love":"sex",
    "moti":"luicca",
    "ok":None
}'''
'''with open("amderinfo.txt","r+") as newinfo:
    newinfo.write(str(a_new_dict))
    json.dump(a_new_dict,newinfo,indent=4)
newinfo.close()'''