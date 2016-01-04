#! /usr/bin/env python

import fileinput
import sys
import argparse

parser = argparse.ArgumentParser('Password Analyser Delimeter')
parser.add_argument('--path',dest='file_path',required=True,help='Enter the file path of the password list to delimit via ":"')
args = parser.parse_args()



print "[+] Opening file " + args.file_path + " for amendment..."

with open(args.file_path, 'r') as f:
    lines = f.readlines()

lines = ['NONE:'+line for line in lines]

with open(args.file_path + "_delimited", 'w') as x:
    x.writelines(lines)

print "[+] File " + args.file_path + "_delimited has been saved."
