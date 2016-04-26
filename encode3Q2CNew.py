#!/usr/bin/env python2
import csv, requests, json, os, re

HEADERS = {'accept': 'application/json'}

listlines = list(csv.reader(open('/Users/ss789/Desktop/test/output.txt', 'rb'), delimiter ='\t'))


listitems = iter(listlines)
next(listitems)

for lines in listitems:

	#print lines[3]

	

	URL = "https://www.encodeproject.org/experiments/"+lines[3]



	#Get the object 
	response =  requests.get(URL, headers = HEADERS)

	#python dict
	response_json_dict = response.json()

	#print response_json_dict
	

	if (k in response_json_dict for k in ('possible_controls')):


		for acc in response_json_dict['possible_controls']:

			if (k in acc for k in ('accession')):
		
				#print lines[3], "\t", lines[0], "\t", acc['accession']

				URLControl = "https://www.encodeproject.org/experiments/"+acc['accession']

				#Get the object
				ControlResponse = requests.get(URLControl, headers = HEADERS)

				#python dict
				ControlResponse_json_dict = ControlResponse.json()

				for each in ControlResponse_json_dict['files']:

					name = os.path.basename(os.path.normpath(each['href']))

					if (name.endswith('.fastq.gz')):

						print lines[0], "\t", name, "\n"


						

					
						
					
						
					






