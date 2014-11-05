# -*- coding: utf-8 -*-

import urllib
import json
from time import sleep

OUTPUT_DIR = 'fb_msg_by_lines2.dat'
THREAD_ID = '484290431649855'
ACCESS_TOKEN = 'CAACEdEose0cBABaRLvU5ZBBXzD7nR2uRraXcgp6D2lkGKZACnLavxynqmvAfDdjwIA2F6RRpXU7UpeyaOHwglQcWKejzpqzEL1C2DDhNuITLERX1UnlsEk0avxZCXq4stFzQn8FwwnjgnyxkHuIqdpmQFk3BZCZCw3SD72HtDLkRlz0qlrhpx6ipRDnmz7ZCJzgPfCiZB38RZCh5whfbd7pscds0PT27SMgZD'
QUERY_TEMPLATE = 'SELECT message_id, body, viewer_id, created_time, author_id , attachment FROM message WHERE thread_id = {0} ORDER BY created_time ASC LIMIT 30 OFFSET {1}'


def get_query(index):
	return QUERY_TEMPLATE.format(THREAD_ID, index)

def get_url(index):
	query = get_query(index);
	params = urllib.urlencode({'q': query, 'access_token': ACCESS_TOKEN})
	url = 'https://graph.facebook.com/fql?' + params
	return url

f = open(OUTPUT_DIR, 'w')
index = 0
error_count = 0
total_count = 0
while True:
	url = get_url(index)
	data = urllib.urlopen(url).read()
	data = json.loads(data);
	if 'data' in data:
		error_count = 0
		for message in data['data']:
			f.write(json.dumps(message))
			f.write('\n')
		index += 30
		total_count += len(data['data'])
		if len(data['data']) = 0:
			break
		print '{0} / {1}'.format(total_count, index)
		sleep(2)
	else:
		print data
		error_count += 1
		if error_count >= 3:
			break

