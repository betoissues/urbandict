#!/usr/sbin/python

import sys
import json
from urllib.request import urlopen

def main():
    if(len(sys.argv) > 1):
        word = '%20'.join(sys.argv[1:])
        data = json.load(urlopen('http://api.urbandictionary.com/v0/define?term=' + word))
        for index in range(3):
            print(str(index+1) + '. ' + data['list'][index]['definition'] + '\n')


if __name__ == "__main__":
    main()
