# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import glob
import os
from collections import defaultdict
import difflib
import time



class rdict(dict):
    def __getitem__(self, key):
        try:
            return super(rdict, self).__getitem__(key)
        except:
            try:
                ret=[]
                for i in self.keys():
                    m= re.match("^"+key+"$",i)
                    if m:ret.append( super(rdict, self).__getitem__(m.group(0)) )
            except:raise(KeyError(key))
        return ret


def writeHtml():
    file.write('<html>\n')
    file.write('<head>\n')
    file.write('<title>Test Code Searcher Report</title>\n')
    file.write('<style>\n')
    file.write('body {\n')
    file.write('    background-color: #456;\n')
    file.write('}\n')
  
    file.write('h1,h2 {\n')
    file.write('    color: white;\n')
    file.write('}\n')

    file.write('td {\n')
    file.write('    border: solid 1px; \n')
    file.write('    padding: 10px; \n')
    file.write('    border-left: 0px;\n')
    file.write('    border-bottom: 0px;\n')
    file.write('    background-color: white;\n')
    file.write('}\n')

    file.write('th {\n')
    file.write('    background-color: #eee;\n')
    file.write('    border: solid 1px;\n')
    file.write('    padding: 10px;\n')
    file.write('    font-weight: normal;\n')
    file.write('    border-left: 0px; \n')
    file.write('    border-bottom: 0px; \n')
    file.write('}\n')

    file.write('table {\n')
    file.write('    border-collapse:  collapse;\n')
    file.write('    border-collapse: separate;\n')
    file.write('    border-spacing: 0;\n')
    file.write('    border-radius: 15px;\n')
    file.write('}\n')

    file.write('mark.red {\n')
    file.write('    background-color: rgb(254, 198, 198);\n')
    file.write('    padding-left: 5px;\n')
    file.write('    padding-right: 5px;\n')
    file.write('}\n')

    file.write('mark.yellow {\n')
    file.write('    background-color: rgb(254, 234, 123);\n')
    file.write('    padding-left: 5px;\n')
    file.write('    padding-right: 5px;\n')
    file.write('}\n')

    file.write('mark.green {\n')
    file.write('    background-color: rgba(190, 252, 190, 0.938);\n')
    file.write('    padding-left: 5px;\n')
    file.write('    padding-right: 5px;\n')
    file.write('}\n')

    file.write('</style>\n')
    file.write('<head>\n')
    file.write('<body>\n')
    file.write('<h1>Test Code Searcher Report</h1>\n')
    

#url
url = "file:///Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0/projects/systems_functions-blind-clones/systems_functions-blind-clones-0.30-classes-withsource.html"

#get html
html = request.urlopen(url)

#set BueatifulSoup
soup = BeautifulSoup(html, "html.parser")

clint = MongoClient('163.221.190.202')
db = clint['testMapList']

codeArray = []
codePathArray = []

startLine = []
stopLine = []

bodyCode = soup.find('body')
# print(bodyCode)

# クローンクラス<h3>の配列を作成し,類似コードが存在するファイルパス<td>を要素として配列に格納する処理

pathToClassDict = defaultdict(list)
classToPathsDict = defaultdict(list)
pathToFragmentDict = defaultdict(list)
pathToCodeInfoDict = defaultdict(list)

try:

    for item in bodyCode.find_all(['h3', 'table']):
        pathArray = []
        if item.name == 'h3':
            cloneclass = item.text.replace('\n','').replace('\r','')
            # print(cloneclass)

        if item.name == 'table':
            # fragmentArray = []      
            tdInfo = item.find_all('td')
            for td in tdInfo:
                codeInfoArray = []
                fragment  = td.find('pre')
                fragmentText = fragment.text
                # print(fragmentText)
                codeInfoArray.append(fragmentText)
                td.find('pre').decompose()
                path = td.text.replace('\n','').replace('\r','')
                pathArray.append(path)

                formalPath = re.sub(r"Lines.*?projects/systems/", "", path)
                codeInfoArray.append(formalPath)
                # print(formalPath)
                path_front = re.sub(r"Lines ", "", path)
                path_line = path_front[:path_front.find('o')]
                path_rmSpace = path_line.replace(' ','')

                startLine = int(path_rmSpace[:path_rmSpace.find('-')])-1
                endLine = int(path_rmSpace[path_rmSpace.find('-')+1:])
                # print(str(startLine) + ':' + str(endLine))
                codeInfoArray.append(startLine)
                codeInfoArray.append(endLine)
                pathToCodeInfoDict[path] = codeInfoArray
                pathToFragmentDict[path] = fragmentText
                # print(pathArray)
                pathToClassDict[path] = cloneclass

            classToPathsDict[cloneclass] = pathArray

    rePathToClassDict = rdict(pathToClassDict)
    classInfo = rePathToClassDict["^(?=.*" + 'projects/systems/a.java' + ").*$"]
    print(classInfo[0])
    pathInfos = classToPathsDict[classInfo[0]]
    print(pathInfos)

    for detected_path in pathInfos:
        if 'projects/systems/a.java' in detected_path:
            input_path = detected_path
            # print(input_path)

    file = open('../TCS_result.html','w')
    writeHtml()
    clone_num = 1
    for key_path in pathInfos:
        # print(key_path)
        if 'projects/systems/a.java' not in key_path:

            code1 = pathToCodeInfoDict[input_path][0][1:].splitlines ()
            code2 = pathToCodeInfoDict[key_path][0][1:].splitlines ()

            diff_lines = difflib.context_diff (code1, code2, 'name-version.orig/test.txt', 'name-version/test.txt', time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime(1212121212)), time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime(1313131313)), 3, '')
    
            twoCodeArray = []
            initLineArray = []
            line_num = 1
            print('-----------------------------------------')
            for diff_line in diff_lines:
                if line_num >= 1 and line_num <= 4:
                    pass
                else:
                    line_init = diff_line[:3]
                    initLineArray.append(line_init)
                    twoCodeArray.append(diff_line)
                line_num += 1
            
            if len(initLineArray) != 0:
                # print(initLineArray)
                separator_num = initLineArray.index('---')
                # print(separator_num)
                print('twoCodeArray : ' + str(len(twoCodeArray)))
                print('initLineArray : ' + str(len(initLineArray)))

                file.write('<h2>Clone Pairs ' + str(clone_num) +'</h2>\n')
                file.write('<table border="1" width=50% height="50" align="center">\n')
                # file.write('<tbody>\n')
                file.write('<tr>\n')
                file.write('<th colspan="5" width="500px" height="50%" align="center">Input Code</th>\n')
                file.write('<th colspan="5" width="500px" height="50%" align="left">\n')
                file.write('Lines ' + str(pathToCodeInfoDict[key_path][2]) + ' - ' + str(pathToCodeInfoDict[key_path][3]) + ' of ' + pathToCodeInfoDict[key_path][1] + '\n')
                file.write('</th>\n')
                file.write('</tr>\n')
                file.write('<tr>\n\n')
                file.write('<td colspan="5" width="500px" height="50%">\n')
                file.write('<pre>\n')

                for line1 in range(0,separator_num):
                    line_mark1 = twoCodeArray[line1][:1]
                    if line_mark1 == '!':
                        file.write('<mark class="red">' + twoCodeArray[line1] + '</mark>' + '\n')
                        # print(twoCodeArray[line1])
                    elif line_mark1 == '+':
                        file.write('<mark class="yellow">' + twoCodeArray[line1] + '</mark>' + '\n')
                    else:
                        file.write(twoCodeArray[line1] + '\n')  

                file.write('</pre>\n')
                file.write('</td>\n')
                file.write('<td colspan="5" width="500px" height="50%">\n')
                file.write('<pre>\n')
                
                for line2 in range(separator_num+1,len(twoCodeArray)):
                    line_mark2 = twoCodeArray[line2][:1]
                    # print(line_mark)
                    if line_mark2 == '!':
                        file.write('<mark class="green">' + twoCodeArray[line2] + '</mark>' + '\n')
                        # print(twoCodeArray[line2])
                    elif line_mark2 == '+':
                        file.write('<mark class="yellow">' + twoCodeArray[line2] + '</mark>' + '\n')
                    else:
                        file.write(twoCodeArray[line2] + '\n')
                
                file.write('</pre>\n')
                file.write('</td>\n')
                file.write('</tr>\n')

                file.write('<tr>\n')
                file.write('<td bgcolor="#FF9966" width="10%" height="10%" align="center">Assertion Roulette</td>\n')
                file.write('<td width="10%" height="10%" align="center">Conditional Test Logic</td>\n')
                file.write('<td width="10%" height="10%" align="center">Constructor Initialization</td>\n')
                file.write('<td bgcolor="#FF9966" width="10%" height="10%" align="center">Default Test</td>\n')
                file.write('<td width="10%" height="10%" align="center">Empty Test</td>\n')
                file.write('<td width="10%" height="10%" align="center">Exception Catching</td>\n\n')
                file.write('<td bgcolor="#FF9966" width="10%" height="10%" align="center">Assertion Roulette</td>\n')
                file.write('<td width="10%" height="10%" align="center">Conditional Test Logic</td>\n')
                file.write('<td width="10%" height="10%" align="center">Constructor Initialization</td>\n')
                file.write('<td width="10%" height="10%" align="center">Default Test</td>\n')
                file.write('</tr>\n')

                print(pathToCodeInfoDict[key_path][1])
                print(pathToCodeInfoDict[key_path][2])
                print(pathToCodeInfoDict[key_path][3])

                items = db.mapingCollection.find({'path':pathToCodeInfoDict[key_path][1],'startline1':int(pathToCodeInfoDict[key_path][2]),'endline1':int(pathToCodeInfoDict[key_path][3])})
           
                for item in items:
                    testline_start = int(item['startline2'])
                    testine_end = int(item['endline2'])
                    testpath = item['testpath']
                    print(testpath)
                    testpath_full = '/Users/ryosuke/Desktop/TCS/0123/' + testpath
                    f = open(testpath_full, "r", encoding="utf-8")
                    lines_origin = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
                    f.close()

                    file.write('<tr>\n')
                    file.write('<th colspan="10" width="500px" height="50%" align="left">\n')
                    file.write('Lines ' + str(testline_start) + ' - ' + str(testine_end) + ' of ' + testpath + '\n')
                    file.write('</th>\n')
                    file.write('</tr>\n')
                    file.write('<tr>\n')
                    file.write('<td colspan="10" width="500px" height="50%">\n')
                    file.write('<pre>\n')
                    
                    for x in range(testline_start,testine_end):
                        file.write(lines_origin[x].replace('\n', '') + '\n')

                    file.write('</pre>\n')
                    file.write('</td>\n')
                    file.write('</tr>\n')
                file.write('</table>')

        clone_num += 1
    
    file.write('</body>\n')
    file.write('</html>\n')

except IndexError:
    print('Could not find similar code.')
    file = open('../TCS_result.html','w')
    
    file.write('<html>\n')
    file.write('<head>\n')
    file.write('<title>Test Code Searcher Report</title>\n')
    file.write('<style>\n')
    file.write('body {\n')
    file.write('    background-color: #456;\n')
    file.write('}\n')
  
    file.write('h1 {\n')
    file.write('    color: white;\n')
    file.write('}\n')

    file.write('</style>\n')
    file.write('<head>\n')
    file.write('<body>\n')
    file.write('<center><h1>Sorry, Not Found Similality Code</h1></center>\n')
    file.write('</body>\n')
    file.write('</html>\n')
