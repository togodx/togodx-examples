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
    if re.search('http://ep.dbcls.jp/togodx-server-pg-dev/build/\?dataset=', line):
        line = re.sub('http://ep.dbcls.jp/togodx-server-pg-dev/build', 'https://togodx.dbcls.jp/human', line)
    print(line)
