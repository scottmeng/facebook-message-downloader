# -*- coding: utf-8 -*-

import urllib
import json
from time import sleep

QUERY_TEMPLATE = 'SELECT message_id, body, viewer_id, created_time, author_id , attachment FROM message WHERE thread_id = 484290431649855 ORDER BY created_time ASC LIMIT 30 OFFSET {0}'

def get_query(index):
	return QUERY_TEMPLATE.format(index)

def get_url(index):
	query = get_query(index);
	params = urllib.urlencode({'q': query, 'access_token': 'CAADlGYxaLrEBAK8dHoMa1wdZCKdZCFhQMmN618WeZCRh7SzwZCIEuobnKCPsZCsaZALZA6CI6pbRwxbRpLcUYoWPZBTVdpiZCP2uGnSR0t8CKEVPbE1GZANT1XqqYmFZCxsZC7s4tdufDIIPLLxgvZCcbaCcNbzzRt43CmTMBYmX8ZAFLjoVxibP37W5ZCyS8uX7lgZAxbB3ZCnvW1IxXSqeKp78D793ZC'})
	url = 'https://graph.facebook.com/fql?' + params
	return url


f = open('fb_msg_by_lines.dat', 'w')
index = 0
error_count = 0
total_count = 0
while True:
	url = get_url(index)
	data = urllib.urlopen(url).read()
	data = json.loads(data);
	if ('data' in data):
		error_count = 0
		for message in data['data']:
			f.write(str(message))
			f.write('\n')
		index += 30
		total_count += len(data['data'])
		print '{0} / {1}'.format(total_count, index)
		sleep(2)
	else:
		print data
		error_count += 1
		if error_count >= 3:
			break

