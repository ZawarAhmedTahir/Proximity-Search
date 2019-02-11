
#Run this code one time to generate testfiles.txt
#testfiles.txt contains all the xml file names


def pathMaker():
    file = open("files.txt","r")
    filer = open("testfile.txt","w")

    list=file.read()
    for i in range (0,len(list)):
        if(list[i:i+19]=="-parscit.130908.xml"):
            print(list[i-14:i+19])
            filer.write(list[i-14:i+19]+'\n')

