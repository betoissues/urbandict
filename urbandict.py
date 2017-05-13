#!/usr/sbin/python

import sys
import json
from urllib.request import urlopen

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        word = sys.argv[1]
        data = json.load(urlopen('http://api.urbandictionary.com/v0/define?term=' + word))
        for index in range(3):
            print(str(index+1) + '. ' + data['list'][index]['definition'] + '\n')
