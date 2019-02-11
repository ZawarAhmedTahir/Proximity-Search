README:
This folder include: 
10 python files.
3 txt files
1 pdf

Running mrthod:
1. Download ACl data Set repo by running zipFileDownloader.py file
	zipFileDownloader.py will download and unzip flders containing XML files
2. run xmlFilePathMaker.py to generate text file which will contain all the paths to xml. It will be later used to generate posting list and poitional indexes.
	xmlFilePathMaker.py uses files.txt to generate paths. This file is given alongside ACL dataset.
3. run postingListV2.py to generate posting list. It will generate posting list and will save in form of pickle for future use.
4. run positionalIndexV3.py to generate posting list. It will generate positional indexes and will save in form of pickle for future use.
5. run distanceProximity.py to search terms using distance operator. Distance operator will be like "~5~" where 5 can be any integer value.
6. withinSentenceProximity.py to search terms using sentece operator. Sentence operator will be like "/s".
7. output for 5 and 6 will be ranked list of documents alongside graphical represntation.

Other files include
1. chainRule.py: Applies chain rule on the query.
2. similarity.py: Resturns cosine cimilarity of qury within documents.
3. plotPie.py: Generates Bar plot graph for visual representation.
4. colorGenerator.py: helper file to genrate colors for plotPie.py and chainRule.py files