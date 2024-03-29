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
  
    file.write('h1 {\n')
    file.write('    margin-top: 25px;\n')
    file.write('    color: white;\n')
    file.write('}\n')

    file.write('h2 {\n')
    file.write('    color: white;\n')
    file.write('}\n')

    file.write('td {\n')
    file.write('    border: solid 1px; \n')
    file.write('    padding: 10px; \n')
    file.write('    border-left: 0px;\n')
    file.write('    border-bottom: 0px;\n')
    file.write('}\n')

    file.write('th {\n')
    file.write('    background-color: #eee;\n')
    file.write('    border: solid 1px;\n')
    file.write('    padding: 10px;\n')
    file.write('    font-weight: normal;\n')
    file.write('    border-left: 0px; \n')
    file.write('    border-bottom: 0px; \n')
    file.write('}\n')

    file.write('mark.red {\n')
    file.write('    background-color: #FFC4C1;\n')
    file.write('    padding-left: 5px;\n')
    file.write('    padding-right: 5px;\n')
    file.write('}\n')

    file.write('mark.yellow {\n')
    file.write('    background-color: rgb(254, 234, 123);\n')
    file.write('    padding-left: 5px;\n')
    file.write('    padding-right: 5px;\n')
    file.write('}\n')

    file.write('mark.green {\n')
    file.write('    background-color: #B5EFDB;\n')
    file.write('    padding-left: 5px;\n')
    file.write('    padding-right: 5px;\n')
    file.write('}\n')

    file.write('mark.grey {\n')
    file.write('    background-color: #EAEEF0;\n')
    file.write('    padding-left: 5px;\n')
    file.write('    padding-right: 5px;\n')
    file.write('}\n')

    file.write('mark.darkred {\n')
    file.write('    background-color: #FF8983;\n')
    file.write('}\n')

    file.write('mark.darkgreen_line {\n')
    file.write('    background-color: #6BDFB8;\n')
    # file.write('    padding-left: 5px;\n')
    # file.write('    padding-right: 5px;\n')
    file.write('}\n')

    file.write('mark.darkred_line {\n')
    file.write('    background-color: #FF8983;\n')
    file.write('}\n')

    file.write('mark.darkgreen {\n')
    file.write('    background-color: #6BDFB8;\n')
    file.write('}\n')

    file.write('.whitecolor {\n')
    file.write('	background-color: white;\n')
    file.write('}\n')

    # file.write('.title {\n')
    # file.write('    font-weight: bold;\n')
    # file.write('}\n')

    file.write('#table-flame {\n')
    file.write('    background-color: rgba(72,72,72,0.4);\n')
    file.write('    padding-left: 35px;\n')
    file.write('    padding-right: 35px;\n')
    file.write('    padding-top: 3px;\n')
    file.write('    padding-bottom: 50px;\n')
    file.write('    -moz-border-radius: 100px;\n')
    file.write('    -webkit-border-radius: 100px;\n')
    file.write('}\n')

    file.write('table, td, th {\n')
    file.write('border: 2px #cccccc solid;\n')
    file.write('}\n')

    file.write('table {\n')
    file.write('  border: 1px solid #aaa;\n')
    file.write('  border-collapse: separate;\n')
    file.write('  border-spacing: 0;\n')
    file.write('  border-radius: 20px;\n')
    file.write('  overflow: hidden;\n')
    file.write('}\n')

    file.write('table thead th,\n')
    file.write('table th,\n')
    file.write('table td {\n')
    file.write('  padding: .6em 3em;\n')
    file.write('  border-bottom: 1px solid #aaa;\n')
    file.write('}\n')

    file.write('table thead th {\n')
    file.write('  background-color: #ddd;\n')
    file.write('}\n')

    file.write('table th {\n')
    file.write('  background-color: #eee;\n')
    file.write('}\n')

    file.write('table thead th + th,\n')
    file.write('table td {\n')
    file.write('  border-left: 1px solid #aaa;\n')
    file.write('}\n')
    
    file.write('table tr:last-child th,\n')
    file.write('table tr:last-child td {\n')
    file.write('  border-bottom: none;\n')
    file.write('}\n')

    file.write('td.leftcode {\n')
    file.write('   border-top: 0px;\n')
    file.write('   border-bottom: none;\n')
    file.write('   padding: 0px;\n')
    file.write('   padding-left: 5%;\n')
    file.write('   height: 5px;\n')
    file.write('}\n')

    file.write('td.rightcode {\n')
    file.write('   border-top: 0px;\n')
    file.write('   border-bottom: 0px;\n')
    file.write('   padding: 0px;\n')
    file.write('   padding-left: 5%;\n')
    file.write('   height: 5px;\n')
    file.write('}\n')

    file.write('pre {\n')
    file.write('   overflow: auto;\n')
    file.write('   white-space: pre-wrap;\n')
    file.write('   word-wrap: break-word;\n')
    file.write('   margin: 0%;\n')
    file.write('}\n')


    file.write('</style>\n')
    file.write('<head>\n')
    file.write('<body>\n')
    file.write('<h1 align="center">Test Code Searcher Report</h1>\n')
    
def countDiff_line(array):
    print('codeList')
    line_diff = 0 
    for code_line in array:
        print(code_line)
        if code_line[:1] == '-' or code_line[:1] == '+' or code_line[:1] == '!': #or code_line[:1] == '!'
            line_diff += 1
    
    return line_diff

def calcUPI(line_diff,line_num):
    upi = line_diff/line_num
    return upi

def generateHTML(sortedItemArray,clone_num):
    # file = open('../TCS_result.html','w')
    writeHtml()
    for num in range(clone_num):
        similarity = round((1 - sortedItemArray[num][0])*100,1)
        if similarity == 100.0:
            similarity = 100
        file.write('<div id="table-flame">\n')
        file.write('<h2 align="center">Clone Pairs ' + str(num + 1) + ' : ' + str(similarity) + '%' + '</h2>\n')
        file.write('<table border="1" width=50% height="50" align="center">\n')
        file.write('<tr>\n')
        file.write('<th class="title" colspan="3" width="500px" height="50%" align="center">Input Code</th>\n')
        file.write('<th class="title" colspan="3" width="500px" height="50%" align="center">Similarity Code</th>\n')            
        file.write('</tr>\n')

        for twofragline_num in range(len(sortedItemArray[num][11])):
            file.write('<tr>\n')
            file.write(sortedItemArray[num][11][twofragline_num] + '\n')
            file.write(sortedItemArray[num][12][twofragline_num] + '\n')
            file.write('</tr>\n')


        # file.write('<tr>\n')
        # file.write('<td class="whitecolor" colspan="3" width="500px" height="50%">\n')
        # file.write('<pre>\n')
       
        # for frag1_line in sortedItemArray[num][11]:
        #     file.write(frag1_line + '\n')
        
        # file.write('</pre>\n')
        # file.write('</td>\n')
        # file.write('<td class="whitecolor" colspan="3" width="500px" height="50%">\n')
        # file.write('<pre>\n')        
        
        # for frag2_line in sortedItemArray[num][12]:
        #     file.write(frag2_line + '\n')
        
        # file.write('</pre>\n')
        # file.write('</td>\n')
        # file.write('</tr>\n')
        file.write('<tr>')
        file.write('<td colspan="6"></td>')
        file.write('</tr>')
        file.write('<tr>')
        file.write('<th colspan="6">Test Suite</th>')
        file.write('</tr>')
        file.write('<tr>\n')
        file.write(sortedItemArray[num][5])
        file.write(sortedItemArray[num][6])
        file.write(sortedItemArray[num][7])
        file.write(sortedItemArray[num][8])
        file.write(sortedItemArray[num][9])
        file.write(sortedItemArray[num][10])

        items = db.mappingCollection_utility.find({'path':sortedItemArray[num][2],'startline1':sortedItemArray[num][3],'endline1':sortedItemArray[num][4]})

        for item in items:
            testline_start = int(item['startline2'])
            testine_end = int(item['endline2'])
            testpath = item['testpath']
            # print(testpath)
            testpath_full = '/Users/ryosuke/Desktop/TCS/0123/' + testpath
            f = open(testpath_full, "r", encoding="utf-8")
            lines_origin = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
            f.close()

            file.write('<tr>\n')
            file.write('<th colspan="6" width="500px" height="50%" align="left">\n')
            file.write('Lines ' + str(testline_start) + ' - ' + str(testine_end) + ' of ' + testpath + '\n')
            file.write('</th>\n')
            file.write('</tr>\n')
            file.write('<tr>\n')
            file.write('<td class="whitecolor" colspan="10" width="500px" height="50%">\n')
            file.write('<pre>\n')

            for x in range(testline_start,testine_end):
                file.write(lines_origin[x].replace('\n', '') + '\n')

            file.write('</pre>\n')
            file.write('</td>\n')
            file.write('</tr>\n')
        file.write('</table>\n')
        file.write('</div>\n')
        file.write('<p></p>')
        file.write('</body>\n')
        file.write('</html>\n')



#url
url = "file:///Users/ryosuke/Desktop/webapp-tcs/cgi-bin/NiCad-5.0/projects/systems_functions-blind-clones/systems_functions-blind-clones-0.30-classes-withsource.html"

#get html
html = request.urlopen(url)

#set BueatifulSoup
soup = BeautifulSoup(html, "html.parser")

# clint = MongoClient('163.221.190.202') #外部サーバーのデータベースにアクセス
clint =MongoClient() #ローカルのデータベースにアクセス
db = clint['testMapList_utility'] 

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

    # file = open('../TCS_result.html','w')
    # writeHtml()
    clone_num = 1

    sortItemDict = defaultdict(list)
    

    for key_path in pathInfos:
        sortItemArray = []
        # print('key_path : ' + key_path)
        if 'projects/systems/a.java' not in key_path:

            code1 = pathToCodeInfoDict[input_path][0][1:].splitlines ()
            code2 = pathToCodeInfoDict[key_path][0][1:].splitlines ()
        
            diff_lines = difflib.context_diff (code1, code2, 'name-version.orig/test.txt', 'name-version/test.txt', time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime(1212121212)), time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime(1313131313)), 100, '')

            twoCodeArray = []
            initLineArray = []
            line_num = 1
            print('-----------------------------------------')
            for diff_line in diff_lines:
                # print(diff_line)
                if line_num >= 1 and line_num <= 4:
                    pass
                else:
                    line_init = diff_line[:3]
                    # print('line_init : ' + line_init)
                    initLineArray.append(line_init)
                    twoCodeArray.append(diff_line)
                line_num += 1
            
            
            if len(initLineArray) != 0:

                separator_num = initLineArray.index('---')
                print('twoCodeArray : ' + str(len(twoCodeArray)))
                print('initLineArray : ' + str(len(initLineArray)))

                code1List = [] 
                line1_num = 0
                for line1 in range(0,separator_num):
                    code1List.append(twoCodeArray[line1])
                    line1_num += 1

                line1_diff = countDiff_line(code1List)

                print('Total line1 diff : ' + str(line1_diff))
                print('Total line1 num  : ' + str(line1_num))
                upi1 = calcUPI(line1_diff,line1_num)
                print('line1 UPI : ' + str(upi1))
                
                
                code2List = []
                line2_diff = 0
                line2_num = 0 
                for line2 in range(separator_num+1,len(twoCodeArray)):
                    code2List.append(twoCodeArray[line2])
                    line2_num += 1

                line2_diff = countDiff_line(code2List)

                print('Total line2 diff : ' + str(line2_diff))
                print('Total line2 num  : ' + str(line2_num))
                upi2 = calcUPI(line2_diff,line2_num)
                print('line2 UPI : ' + str(upi2))

                if upi1 >= upi2:
                    UPI = upi1
                else:
                    UPI = upi2
                print('UPI : ' + str(UPI))

                sortItemArray.append(UPI)

                if len(code1List) >= len(code2List):
                    code_row = len(code1List)
                else:
                    code_row = len(code2List)

                index = 0
                code_row = len(code2List)
                start = 0
                while index <=100:
                    index += 1
                    for row_num in range(start+1,code_row):
                        if code1List[row_num][:1] != code2List[row_num][:1]:
                            start = row_num
                            if code1List[row_num][:1] == '!' or code1List[row_num][:1] == '+' or code1List[row_num][:1] == '-':
                                code2List.insert(row_num,'*')
                                if len(code1List) <= len(code2List):
                                    code_row = len(code1List)
                                else:
                                    code_row = len(code2List)
                                
                            elif code1List[row_num][:1] == ' ':
                                code1List.insert(row_num,'*')
                                if len(code1List) <= len(code2List):
                                    code_row = len(code1List)
                                else:
                                    code_row = len(code2List)
                        else:
                            pass

                # print('code1List')
                # for code1 in code1List:
                #     print(code1)

                # print('code2List')
                # for code2 in code2List:
                #     print(code2)

                # file.write('<tr>\n\n')
                # file.write('<td class="whitecolor" colspan="3" width="500px" height="50%">\n')
                # file.write('<pre>\n')                         

                max_row1 = 0
                for code_item in code1List:
                    code_formal = code_item.replace('\t','   ')
                    if max_row1 <=len(code_formal):
                        max_row1 = len(code_formal)

                print('code1_new_words')
                code1_words_Array = []
                code1_num = 0
                for code1_new in code1List:
                    code1_new_words = code1_new.split()
                    print(code1_new_words)
                    code1_words_Array.append(code1_new_words)
                    code1_num += 1
                    
                print('code2_new_words')
                code2_words_Array = []
                code2_num = 0
                for code2_new in code2List:
                    code2_new_words = code2_new.split()
                    print(code2_new_words)
                    code2_words_Array.append(code2_new_words)
                    code2_num += 1

                code1List_highlight = []
                code2List_highlight = []
                if code1_num == code2_num:
                    for num in range(code1_num):     
                        if code1_words_Array[num][0] == '!' and code2_words_Array[num][0] == '!':
                            if len(code1_words_Array[num]) >= len(code2_words_Array[num]):
                                words_num = len(code2_words_Array[num])
                            else:
                                words_num = len(code1_words_Array[num])

                            print(code1_words_Array[num])
                            print(code2_words_Array[num])
                            print('words num : ' + str(words_num))
                            if words_num == 1:
                                code1List_highlight.append(code1List[num])
                                code2List_highlight.append(code2List[num])
                            else:
                                # print(num)
                                not_equal = 0    
                                for word in range(words_num):
                                    if code1_words_Array[num][word] == code2_words_Array[num][word]:
                                        print('Match! ' + str(not_equal))
                                    
                                    else:
                                        not_equal += 1
                                        print('Not Match! '+ str(not_equal))
                                        if not_equal >= 2:
                                            # print(num)
                                            code1List_highlight[num] = '<mark class="darkred_line">' + code1List[num] + '</mark>'
                                            code2List_highlight[num] = '<mark class="darkgreen_line">' + code2List[num] + '</mark>'
                                            
                                        else:    
                                            print('Not equal : ' + str(num) + ' : "'+ code1_words_Array[num][word] + '" != "' + code2_words_Array[num][word] + '"')
                                            code1_highline = code1List[num].replace(code1_words_Array[num][word], '<mark class="darkred">' + code1_words_Array[num][word] + '</mark>')
                                            code2_highline = code2List[num].replace(code2_words_Array[num][word], '<mark class="darkgreen">' + code2_words_Array[num][word] + '</mark>')
                                            print(code1_highline)
                                            print(code2_highline)
                                            code1List_highlight.append(code1_highline)
                                            code2List_highlight.append(code2_highline)              
                                        
                        else:
                            code1List_highlight.append(code1List[num])
                            code2List_highlight.append(code2List[num])

                items = db.mappingCollection_utility.find({'path':pathToCodeInfoDict[key_path][1],'startline1':int(pathToCodeInfoDict[key_path][2]),'endline1':int(pathToCodeInfoDict[key_path][3])})
                smell_count = 0
            
                for smell in items[0].values():
                    # print(smell)
                    if smell == 'TRUE':
                        smell_count += 1
                print('smell_count : ' + str(smell_count))
                sortItemArray.append(smell_count)
                print(sortItemArray)

                sortItemArray.append(pathToCodeInfoDict[key_path][1])
                sortItemArray.append(int(pathToCodeInfoDict[key_path][2]))
                sortItemArray.append(int(pathToCodeInfoDict[key_path][3]))

                if items[0]['Assertion Roulette'] == 'TRUE':
                    sortItemArray.append('<td bgcolor="#FF9966" width="10%" height="5spx" align="center">Assertion Roulette</td>')
                
                else:
                    sortItemArray.append('<td class="whitecolor" width="10%" height="5spx" align="center">Assertion Roulette</td>')

                if items[0]['Conditional Test Logic'] == 'TRUE':
                    sortItemArray.append('<td bgcolor="#FF9966" class="whitecolor" width="10%" height="5px" align="center">Conditional Test Logic</td>')
                
                else:
                    sortItemArray.append('<td class="whitecolor" width="10%" height="5px" align="center">Conditional Test Logic</td>')
                
                if items[0]['Default Test'] == 'TRUE':
                    sortItemArray.append('<td bgcolor="#FF9966" class="whitecolor" width="10%" height="5px" align="center">Default Test</td>')
                
                else:
                    sortItemArray.append('<td class="whitecolor" width="10%" height="5px" align="center">Default Test</td>')
                
                if items[0]['Eager Test'] == 'TRUE':
                    sortItemArray.append('<td bgcolor="#FF9966" width="10%" height="5px" align="center">Eager Test</td>')
                
                else:
                    sortItemArray.append('<td class="whitecolor" width="10%" height="5px" align="center">Eager Test</td>')
                
                if items[0]['Exception Catchingowing'] == 'TRUE':
                    sortItemArray.append('<td bgcolor="#FF9966" class="whitecolor" width="10%" height="5px" align="center">Exception Handling</td>')
           
                else:
                    sortItemArray.append('<td class="whitecolor" width="10%" height="5px" align="center">Exception Handling</td>')

                if items[0]['Mystery Guest'] == 'TRUE':
                    sortItemArray.append('<td bgcolor="#FF9966" class="whitecolor" width="10%" height="5px" align="center">Mystery Guest</td>')
              
                else:
                    sortItemArray.append('<td class="whitecolor" width="10%" height="5px" align="center">Mystery Guest</td>')

                print(sortItemArray)

                code1List_output = []
                print('code1List_highlight')
                for code1_line in code1List_highlight:
                    print(code1_line)
                    code1_line = code1_line.replace('\t','   ')
                    add_spc = max_row1 - len(code1_line)
                    line_mark1 = code1_line[:1]
                    if line_mark1 == '!':
                        # file.write('<mark class="red">' + code1_line + '</mark>' + '\n')
                        code1List_output.append('<td class="leftcode" bgcolor="#FFC4C1" colspan="3"><pre>' + code1_line + '</pre></td>')
                        line1_diff += 1
                    elif line_mark1 == '+':
                        # file.write('<mark class="yellow">' + code1_line + '</mark>' + '\n')
                        code1List_output.append('<td class="leftcode" bgcolor="#feea7b" colspan="3"><pre>' + code1_line + '</pre></td>')
                        line1_diff += 1
                    elif line_mark1 == '-':
                        # file.write('<mark class="red">' + code1_line + '</mark>' + '\n')
                        code1List_output.append('<td class="leftcode" bgcolor="#FFC4C1" colspan="3"><pre>' + code1_line + '</pre></td>')
                        line1_diff += 1
                    elif line_mark1 == '*':
                        # for add_num in range(add_spc):
                        #     code1_line = code1_line + '  '
                        # file.write('<mark class="grey">' + code1_line + '</mark>' + '\n')
                        code1List_output.append('<td class="leftcode" bgcolor="#EAEEF0" colspan="3"><pre>' + code1_line + '</pre></td>')
                        line1_diff += 1
                    else:
                        # file.write(code1_line + '\n')
                        code1List_output.append('<td class="leftcode" bgcolor="#fbfbfb" colspan="3"><pre>' + code1_line + '</pre></td>')   

                code2List_output = []
                max_row2 = 0
                for code_item in code2List:
                    if max_row2 <=len(code_item):
                        max_row2 = len(code_item)

                print('code2List_highlight')
                for code2_line in code2List_highlight:
                    print(code2_line)
                    code2_line = code2_line.replace('\t','   ')
                    add_spc = max_row2 - len(code2_line)
                    line_mark2 = code2_line[:1]
                    if line_mark2 == '!':
                        # file.write('<mark class="green">' + code2_line + '</mark>' + '\n')
                        code2List_output.append('<td class="rightcode" bgcolor="#B5EFDB" colspan="3"><pre>' + code2_line + '</pre></td>')
                        line2_diff += 1
                    elif line_mark2 == '+':
                        # file.write('<mark class="yellow">' + code2_line + '</mark>' + '\n')
                        code2List_output.append('<td class="rightcode" bgcolor="#feea7b" colspan="3"><pre>' + code2_line + '</pre></td>')
                        line2_diff += 1
                    elif line_mark2 == '-':
                        # file.write('<mark class="green">' + code2_line + '</mark>' + '\n')
                        code2List_output.append('<td class="rightcode" bgcolor="#B5EFDB" colspan="3"><pre>' + code2_line + '</pre></td>')
                        line2_diff += 1
                    elif line_mark2 == '*':
                        # for add_num in range(add_spc):
                            # code2_line = code2_line + '  '
                        # file.write('<mark class="grey">' + code2_line + '</mark>' + '\n')
                        code2List_output.append('<td class="rightcode" bgcolor="#EAEEF0" colspan="3"><pre>' + code2_line + '</pre></td>')
                        line2_diff += 1
                    else:
                        # file.write(code2_line + '\n')
                        code2List_output.append('<td class="rightcode" bgcolor="#fbfbfb" colspan="3"><pre>' + code2_line + '</pre></td>')

                print('code1List_output')
                for code1_output_line in code1List_output:
                    print(code1_output_line)

                print('code2List_output')
                for code2_output_line in code2List_output:
                    print(code2_output_line)

                sortItemArray.append(code1List_output)
                sortItemArray.append(code2List_output)
                print('sortItemArray ' + str(len(sortItemArray)))
                sortItemDict[key_path] = sortItemArray

    for i in sortItemDict:
        print(i)
        print(sortItemDict[i][0])
        print(sortItemDict[i][1])
    
    code_sorted = sorted(sortItemDict.items(), key=lambda x: (x[1][0], -x[1][1]))
    sortedItemArray = []
    for sorted_key in code_sorted:
        # print(sorted_key[1])
        sortedItemArray.append(sorted_key[1])
    print(sortedItemArray)
    codefrag_num = len(sortedItemArray)

    file = open('../TCS_result.html','w')
    generateHTML(sortedItemArray,codefrag_num)

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
    file.write('    margin-top: 50px;\n')
    file.write('    color: white;\n')
    file.write('}\n')

    file.write('</style>\n')
    file.write('<head>\n')
    file.write('<body>\n')
    file.write('<center><h1>Sorry, Not Found Similality Code</h1></center>\n')
    file.write('</body>\n')
    file.write('</html>\n')

