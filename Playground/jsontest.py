# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:40:06 2019

@author: kuifenhu
"""

import json 
with open('test.json') as data_file:
    r = json.load(data_file)
loaded_r = json.loads(r)


data['Value']=d.ts_result[0]

import json
with open('write.json', 'w') as outfile:
    json.dump(data, outfile, sort_keys=False, indent=4)
    
import json

r = {'is_claimed': 'True', 'rating': 3.5}
r = json.dumps(r)
loaded_r = json.loads(r)
loaded_r['rating'] #Output 3.5
type(r) #Output str
type(loaded_r) #Output dict

#save ndarrary into csv
import numpy as np
np.savetxt('./data/foo.csv',d.ts_result[0],delimiter=',')

# save dict to array

import csv
toCSV = [{'name':'bob','age':25,'weight':200},
         {'name':'jim','age':31,'weight':180}]
keys = toCSV[0].keys()
with open('people.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)
    
    