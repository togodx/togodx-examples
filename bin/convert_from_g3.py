#!/usr/bin/env python3
import sys
import argparse
import re

parser = argparse.ArgumentParser(description='Convert example.md')
parser.add_argument('markdown', help='Markdown file')
args = parser.parse_args()

fp = open(args.markdown, 'r')
for line in fp:
    line = line.rstrip()
    if re.search('https://togodx-attribute-g3.dbcls.jp/human/\?togoKey=', line):
        line = re.sub('https://togodx-attribute-g3.dbcls.jp', 'https://togodx.dbcls.jp', line)
        line = re.sub('\?togoKey=', '?dataset=', line)
        line = re.sub('&keys=', '&annotations=', line)
        line = re.sub('&values=', '&filters=', line)
        line = re.sub('%2C%22ids%22%3A', '%2C%22nodes%22%3A', line)
        line = re.sub('%7B%22categoryId%22', '%7B%22node%22', line)
    print(line)
