#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import requests
from bs4 import BeautifulSoup 

# process variables
app_list = ('comptext','comptty','flamp','fldigi','fllog','flmsg','flnet','flrig','flwkey','flwrap','linsim')
alpha_url = "http://sourceforge.net/projects/fldigi/files/alpha_tests/"
test_url = "https://sourceforge.net/projects/fldigi/files/test_suite/"
release_url ="https://sourceforge.net/projects/fldigi/files/"

# clear the screen
def clear_screen():
    """Clear based on the platform"""
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

if sys.platform == "win32":
    ext = ("zip" + "/download")
else:
    ext = ("gz" + "/download")

# generate alpha list versions
def alpha_list():
    source = requests.get(alpha_url)
    data = source.text
    soup = BeautifulSoup(data)

    print("Generating Alpha List")
    print("---------------------")
    for line in soup.findAll('a'):
        if line.has_attr('href'):
            if(line['href'].endswith(ext)):
                a1 = str(line['href'])
                af = a1.split("alpha_tests/", 1)[1][:-9]
                an = af.split("-", 1)[0]
                av = af.split("-", 1)[1][:-7]
                print(an + " " + av)
    print()

# generate test suite versions
def test_list():
    source = requests.get(test_url)
    data = source.text
    soup = BeautifulSoup(data)

    print("Generating TestSuite List")
    print("--------------------------")
    for line in soup.findAll('a'):
        if line.has_attr('href'):
            if(line['href'].endswith(ext)):
                a1 = str(line['href'])
                af = a1.split("test_suite/", 1)[1][:-9]
                tn = af.split("-", 1)[0]
                tv = af.split("-", 1)[1][:-7]
                print(tn + " " + tv)
    print()

# generate release application versions
def release_list():
    print("Generating Release List")
    print("-----------------------")
    for p in app_list:
        source = requests.get(release_url + p)
        data = source.text
        soup = BeautifulSoup(data)

        for line in soup.findAll('a'):
            if line.has_attr('href'):
                if(line['href'].endswith(ext)):
                    a1 = str(line['href'])
                    af = a1.split("files/" + p + "/", 1)[1][:-9]
                    rn = af.split("-", 1)[0]
                    rv = af.split("-", 1)[1][:-7]
                    print(rn + " " + rv)
    print()

if __name__ == "__main__":
    clear_screen()
    alpha_list()
    test_list()
    release_list()
