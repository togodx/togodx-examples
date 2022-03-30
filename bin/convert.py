#!/usr/bin/env python3
import sys
import argparse
import re

parser = argparse.ArgumentParser(description='Convert example.md')
parser.add_argument('markdown', help='Markdown file')
parser.add_argument('--g3', action='store_true', help='togodx-attribute-g3.dbcls.jp')
parser.add_argument('--kohan', action='store_true', help='ep.dbcls.jp')
args = parser.parse_args()

fp = open(args.markdown, 'r')
header = []
for line in fp:
    line = line.rstrip()
    if re.search('https://togodx.dbcls.jp/human/\?togoKey=', line):
        if args.g3:
            line = re.sub('togodx.dbcls.jp', 'togodx-attribute-g3.dbcls.jp', line)
        elif args.kohan:
            line = re.sub('https://togodx.dbcls.jp/human', 'http://ep.dbcls.jp/togodx-server-kohan-pg/build', line)
            line = re.sub('\?togoKey=', '?dataset=', line)
            line = re.sub('&keys=', '&annotations=', line)
            line = re.sub('&values=', '&filters=', line)
            line = re.sub('%7B%22attributeId%22%3A', '%7B%22attribute%22%3A', line)
            line = re.sub('%2C%22ids%22%3A', '%2C%22nodes%22%3A', line)
            line = re.sub('%7B%22categoryId%22', '%7B%22node%22', line)
            line = re.sub('%22ancestors%22', '%22path%22', line)
        print(line)
    else:
        print(line)
