#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import os
import subprocess, sys
import shutil
import glob
import codecs
import sys
import contextlib

@contextlib.contextmanager
def redirect_stdout(target):
    original = sys.stdout
    sys.stdout = target
    yield
    sys.stdout = original

form = cgi.FieldStorage()
text = form.getvalue('text','')
# print(html_body % (text))


file = open('/Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0/projects/systems/a.java','w')
file.write(text)
file.close()

with redirect_stdout(open(os.devnull, 'w')):
    os.chdir('/Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0')

    cp = subprocess.run(['./nicad5', 'functions', 'java', 'projects/systems', 'default-report'], stdout=subprocess.PIPE)

    os.chdir('/Users/ryosuke/Desktop/webapp-tcs/cgi-bin/')
    # print(os.getcwd())

    os.system('python cgi-generation.py')

    shutil.rmtree("/Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0/projects/systems_functions-blind-clones")
    print('Deleted NiCad generation folder!')

    NICAD_functionPath_xml = glob.glob('/Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0/projects/*.xml')
    for functionPath_xml in NICAD_functionPath_xml:
        os.remove(functionPath_xml)
    print('Deleted xml file!')

    NICAD_functionPath_log = glob.glob('/Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0/projects/*.log')
    for functionPath_log in NICAD_functionPath_log:
        os.remove(functionPath_log)
    print('Deleted log file!')

# 初回ロード時
if form.list == []:
    html = codecs.open('../TCS_result.html', 'r', 'utf-8').read()
# SUBMITボタン押下時
else:
    html = codecs.open('../TCS_result.html', 'r', 'utf-8').read()

print("")
print(html)

os.remove('/Users/ryosuke/Desktop/webapp-tcs/TCS_result.html')
print('Deleted TCS_result file!')