# -*- coding: utf-8 -*-

import urllib
import json

INPUT_DIR = 'fb_msg_by_lines2.dat'

with open(INPUT_DIR, 'r') as f:
	lines = f.readlines()
	for line in lines:
		line = json.loads(line)
		print line['body']
