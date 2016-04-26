#!/usr/bin/env python2

''' Get results of search from ENCODE server'''

import requests, json

# json format output
HEADERS = {'accept': 'application/json'}

# search for ChIP-seq assay released in Aug 2012
URL = "https://www.encodeproject.org/search/?type=Experiment&assay_title=ChIP-seq&month_released=August%2C+2012&frame=object&limit=all"

# search result 
response = requests.get(URL, headers=HEADERS)

# JSON response as python dict
response_json_dict = response.json()

#print the object
#print json.dumps(response_json_dict, indent=4, separators=(',', ': '))

Dataset = response_json_dict

def fun(ds):

	
	for obj in ds['@graph']:
		
		if all(k in obj for k in ('target','replicates','accession','biosample_term_name')):
			
			# protein target
			target_URI = obj['target']
			target_response = requests.get('https://www.encodeproject.org/'+target_URI, headers=HEADERS)
			target = target_response.json()


			# no. of replicates
			NoOfReplicates = len(obj['replicates'])

			
			print obj['accession'], "\t", obj['biosample_term_name'], "\t", target['label'], "\t", NoOfReplicates, "\n"

	
		
fun(Dataset)








