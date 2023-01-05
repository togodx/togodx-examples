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
    if re.search('https://togodx.dbcls.jp/human', line):
        line = re.sub('https://togodx.dbcls.jp/human', 'http://ep.dbcls.jp/togodx-server-pg-dev/build', line)
    print(line)
