from xml.dom import minidom
import pickle
from nltk import word_tokenize
from nltk.corpus import stopwords
import datetime
stopSet=list(stopwords.words('english'))
posting_list={'':''}
import time
start = time.time()



def invertedIndexCreator():
    print("Indexing")
    file = open("trimedFileNames.txt","r")
    file_list=file.readlines()
    for i in range (0,len(file_list)):
        file_name = file_list[i].replace('\n', '')
        print(file_name)
        mydoc = minidom.parse(file_name)
        items = mydoc.getElementsByTagName('bodyText')
        rawData = ""
        for elem in items:
            rawData += (elem.firstChild.data)
        tokens = word_tokenize(rawData)



        for i in range (0,len(tokens)):
            try:
                str=tokens[i]
                if(str[0]=='-' or str[0]=="'"):
                    try:
                        tokens[i]=str[1:len(str)]
                    except:
                        None
                str=tokens[i]
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
                if str.__contains__("-") :
                    if str[len(str) - 1] == '-':
                        try:
                            tokens[i] = tokens[i].replace('-', tokens[i + 1])
                            tokens[i + 1] = '$//$'
                        except:
                            None
                    else:
                        tokens[i]="$//$"
                        splitList=str.split("-")
                        tokens.extend(splitList)
            except:
                None
        for w in tokens:
            if not w is "$//$":
                try:
                    posting_list.setdefault(w.lower(), []).append(file_name)
                except:
                    None





def duplicateRemover(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


invertedIndexCreator()

for tm in posting_list:
    posting_list[tm]=duplicateRemover(posting_list[tm])
done = time.time()
elapsed1 = done - start


start = time.time()
#pickle.dump(posting_list, open("postingPickles/postigListObjectV3.pickle", "wb"))    #saves inverted list in form of object for future use (Saves time)

done = time.time()
elapsed = done - start

for tm in posting_list:
    print(tm, posting_list[tm])     #Print inverted index
print(elapsed1)
print(elapsed)