from collections import defaultdict

from PyPDF2 import PdfFileReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from xml.dom import minidom
filesListName = list()

def most_element(liste):
    numeral=[[liste.count(nb), nb] for nb in liste]
    numeral.sort(key=lambda x:x[0], reverse=True)
    return(numeral[0][1])

def ranker(term,docList):
    returnDict= defaultdict(dict)
    tmList=list()
    tmList.append(term)
    docnameList=list(docList)
    for doc in docList:
        mydoc = minidom.parse(doc)
        items = mydoc.getElementsByTagName('bodyText')
        rawData = ""
        for elem in items:
            rawData += (elem.firstChild.data)
        tmList.append(rawData)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix_train = tfidf_vectorizer.fit_transform(tmList)

    tmpList=cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train)[0]
    j=1
    for i in docnameList:
        returnDict.setdefault(i, []).append(tmpList[j])
        j+=1
    from collections import OrderedDict
    returnDict = OrderedDict(sorted(returnDict.items(), key=lambda x: x[1],reverse=True))
    return returnDict

