import shutil
import glob
import os


shutil.rmtree("/Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0/projects/systems_functions-blind-clones")
NICAD_functionPath_xml = glob.glob('/Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0/projects/*.xml', recursive=True)
print(NICAD_functionPath_xml)
for functionPath_xml in NICAD_functionPath_xml:
    os.remove(functionPath_xml)

NICAD_functionPath_log = glob.glob('/Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0/projects/*.log', recursive=True)
for functionPath_log in NICAD_functionPath_log:
    os.remove(functionPath_log)
print(NICAD_functionPath_log)