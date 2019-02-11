import pickle
from collections import defaultdict
from xml.dom import minidom
from more_itertools import locate

posting_list = pickle.load(open("postingPickles/postigListObjectV3.pickle", "rb"))
positional_list = pickle.load(open("postingPickles/positionListObjectV3.pickle", "rb"))


def printPosition(token):
    for tn in positional_list[token]:
        print("    " + tn + ': ' + str(positional_list[token][tn]))
    return positional_list[token]


def printPosting(token):
    return posting_list[token]





def getDocName(docID):
    mydoc = minidom.parse(docID)
    items = mydoc.getElementsByTagName('title')
    return items[0].firstChild.data.replace("\n", "")


sentenceTokenCompound = defaultdict(dict)
query = input("\nEnter Query: ")
#query = "natural ~5~ language"

queryList = query.split(" ")
queryList = [x.lower() for x in queryList]
distTemp = 0
for q in queryList:
    if q.__contains__("~"):
        distTemp = int(q.replace("~", ""))
        i = queryList.index(q)
        del queryList[i]

setDocList = []
for term in queryList:
    docNameList = []
    for tn in posting_list[term]:
        docNameList.append(tn)
    setDocList.append(set(docNameList))
intersectDocList = set.intersection(*setDocList)

proximityResult = defaultdict(dict)
termSetList = list()
flag = 0
termList = []
for doc in intersectDocList:

    for term in queryList:
        termList.append(positional_list[term][doc])
    for i in range(0, len(termList)):

        if (len(termList[0]) < len(termList[1])):
            for t0 in termList[0]:
                for t1 in termList[1]:
                    if ((t1 < t0 + distTemp and t1 > t0)):
                        flag = 1
                        proximityResult[doc] = [t0, t1]
        elif (len(termList[0]) >= len(termList[1])):
            for t1 in termList[0]:
                for t0 in termList[1]:
                    if ((t1 < t0 + distTemp and t1 > t0)):
                        flag = 1
                        proximityResult[doc] = [t0, t1]

docKeys = list()
for i in proximityResult.keys():
    docKeys.append(i)
from similarity import ranker

queryStr = " ".join(queryList)
orderDict = ranker(queryStr, docKeys[:10])

i = 0
from plotPie import plotPieBar

if flag == 1:

    print("Searched Query: '" + query + "' found! \n")
    for tm in orderDict:
        if (i == 10):
            break
        print(str(i) + ". " + tm + ", Total hits in document: " + " -- ", orderDict[tm][0])

        i += 1
    plotPieBar(orderDict, query)
else:
    print("Searched Query not found! \n")
