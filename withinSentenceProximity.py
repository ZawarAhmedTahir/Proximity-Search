import pickle
from collections import defaultdict
from xml.dom import minidom

posting_list = pickle.load(open("postingPickles/postigListObjectShort.pickle", "rb"))
positional_list = pickle.load(open("postingPickles/positionListObjectShort.pickle", "rb"))


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
queryList=query.split(" /s ")
queryList=[x.lower() for x in queryList]
print(queryList)
queryList = [x.lower() for x in queryList]
distTemp = 0

setDocList = []
for term in queryList:
    docNameList = []
    for tn in posting_list[term]:
        docNameList.append(tn)
    setDocList.append(set(docNameList))
intersectDocList = set.intersection(*setDocList)
# print(intersectDocList)

proximityResult = defaultdict(dict)
termSetList = list()
flag = 0
termList = []
dotList=defaultdict(dict)
for doc in intersectDocList:
    dotList[doc] = positional_list["."][doc]
tempList=dict()
finalDocList=list()
for doc in dotList:
    tempList.setdefault(doc, []).append(dotList[doc])
    for dc in tempList[doc]:
        tempList2 = dict()
        for term in queryList:
            tempList2.setdefault(term, []).append(positional_list[term][doc])
        for i in range (0,len(dc)-1):
            for term in queryList[0:1]:
                for ind in tempList2[term][0]:
                    if (ind <dc[i+1] and ind >dc[i]):
                        for term2 in queryList[1:]:
                            for ind2 in tempList2[term2][0]:
                                if (ind2 < dc[i + 1] and ind2 > dc[i]):
                                    flag=1
                                    finalDocList.append(doc)

print(finalDocList)



resultList = defaultdict(dict)

from similarity import ranker
queryStr=" ".join(queryList)
if(len(finalDocList)>10):
    orderDict=ranker(queryStr, finalDocList[:10])
else:
    orderDict = ranker(queryStr, finalDocList)


i=0
from plotPie import plotPieBar
if flag == 1:

    print("Searched Query: '"+query+"' found! \n")
    for tm in orderDict:
        if(i==10):
            break
        #print(str(i)+". "+str(getDocName(tm))[:20]+ ", Total hits in document: "+str(len(intersectSentenceList[tm][0])))
        print(str(i)+". "+tm+ ", Total hits in document: "+", ","Cosine Similarity: ",orderDict[tm][0])


        i+=1
    plotPieBar(orderDict,query)
else:
    print("Searched Query not found! \n")

