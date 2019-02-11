from pydoc import locate
from collections import defaultdict
from more_itertools import locate
from xml.dom import minidom
import pickle
from nltk import word_tokenize

positional_list = defaultdict(dict)
positional_list[""][""] = []
import time
start = time.time()
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
def xmlFileReader():
    file = open("trimedFileNames.txt","r")
    file_list=file.readlines()
    for i in range (0,len(file_list)):

        file_name = file_list[i].replace('\n', '')

        print(file_name)
        mydoc = minidom.parse(file_name)
        items = mydoc.getElementsByTagName('bodyText')

        rawData = ""
        for elem in items:
            rawData += (elem.firstChild.data)+"\n"
        tokens = word_tokenize(rawData)
        #tokens = normalise(tokens, verbose=True)

        for i in range (0,len(tokens)):
            try:
                str=tokens[i]
                if(str[0]=='-' or str[0]=="'"):
                    try:
                        tokens[i]=str[1:len(str)]
                    except:
                        None
                #if(str[len(str)-1]=='*' or str[len(str)-1]=='.' or str[len(str)-1]==","):
                #    tokens[i]=str[0:len(str)-1]
                str=tokens[i]
                #print(str)
                if (str[0] == '*'):
                    tokens[i] = str[1:len(str)]
                str = tokens[i]
                if str.__contains__("_") :
                    if str[len(str) - 1] == '_':
                        try:
                            tokens[i] = tokens[i].replace('_',"")
                            tokens.extend(tokens[i+1])
                        except:
                            None

                    else:
                        tokens[i]="$//$"
                        splitList=str.split("_")
                        tokens.extend(splitList)
                #if((len(str)==1 or(len(str)==2 and str[len(str)-1] == ".")) and str != 'a'):
                #    tokens[i]='$'
                if str.__contains__("-") :
                    if str[len(str) - 1] == '-':
                        try:
                            tokens[i] = tokens[i].replace('-', tokens[i + 1])
                            tokens[i + 1] = '$'
                        except:
                            None
                    else:
                        tokens[i]="$//$"
                        splitList=str.split("-")
                        tokens.extend(splitList)
            except:
                None

        ''''''
        words = list(set(tokens))


        for w in words:
            if not w is "$//$":
                try:
                    indices = list(locate(tokens, lambda x: x == w))
                    if (len(indices) >= 1):
                        positional_list[w.lower()][file_name] = indices
                except:
                    None



xmlFileReader()
done = time.time()
elapsed1 = done - start
start = time.time()


#pickle.dump(positional_list, open("postingPickles/positionListObjectV3.pickle", "wb"))


done = time.time()
elapsed = done - start


for tm in positional_list:
    print(tm)
    for tn in positional_list[tm]:
        print("    " + tn + ': ' + str(positional_list[tm][tn]))

print(elapsed1)
print(elapsed)