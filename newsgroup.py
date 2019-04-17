'''
processing the special format used by the Cranfield Dataset
'''
from doc import Document
import os
import glob
from fnmatch import fnmatch

class NewsGroup:
    def __init__(self, files):
        self.docs = []
        self.class1items1 = []
        self.class1items2 = []
        self.class1items3 = []
        self.class1items4 = []
        self.class1items5 = []
        self.class1items6 = []
        #find class id based on document number
        self.classDocumentLookup ={}
        # this part will handle document with duplicate names
        for filename in files:
            newsGroupFile = open(filename)
            head, tail = os.path.split(filename)
            if head.find("comp.graphics") != -1:
                docid = tail+"comp.graphics"
            if head.find("comp.os.ms-windows.misc")!= -1:
                docid = tail + "comp.os.ms-windows.misc"
            if head.find("comp.sys.ibm.pc.hardware")!= -1:
                docid = tail + "comp.sys.ibm.pc.hardware"
            if head.find("comp.sys.mac.hardware")!= -1:
                docid = tail + "comp.sys.mac.hardware"
            if head.find("comp.windows.x")!= -1:
                docid = tail + "comp.windows.x"
            if head.find("rec.autos")!= -1:
                docid = tail + "rec.autos"
            if head.find("rec.motorcycles")!= -1:
                docid = tail + "rec.motorcycles"
            if head.find("rec.sport.baseball")!= -1:
                docid = tail + "rec.sport.baseball"
            if head.find("rec.sport.hockey")!= -1:
                docid = tail + "rec.sport.hockey"
            if head.find("sci.crypt")!= -1:
                docid = tail + "sci.crypt"
            if head.find("sci.electronics")!= -1:
                docid = tail + "sci.electronics"
            if head.find("sci.med")!= -1:
                docid = tail + "sci.med"
            if head.find("sci.space")!= -1:
                docid = tail + "sci.space"
            if head.find("misc.forsale")!= -1:
                docid = tail + "misc.forsale"
            if head.find("talk.politics.misc")!= -1:
                docid = tail + "talk.politics.misc"
            if head.find("talk.politics.guns")!= -1:
                docid = tail + "talk.politics.guns"
            if head.find("talk.politics.mideast")!= -1:
                docid = tail + "talk.politics.mideast"
            if head.find("talk.religion.misc")!= -1:
                docid = tail + "talk.religion.misc"
            if head.find("alt.atheism")!= -1:
                docid = tail + "alt.atheism"
            if head.find("soc.religion.christian")!= -1:
                docid = tail + "soc.religion.christian"
            totalNumberofLines = 0
            with open(filename) as f:
                for i, l in enumerate(f):
                    pass
                totalNumberofLines = i + 1
            #print (totalNumberofLines)
            subject = ''
            message = ''
            startread = False
            buf = ''
            linecounter = 0
            numOfLinesToRead = 0
            for line in newsGroupFile:
                #print (line)

                linecounter = linecounter+1
                if 'Subject:' ==str(line[0:8]):
                    subject = line[9:] # got title
                if 'Lines:'==str(line[0:6]):
                   # print (line[7])
                    if line[8]=='\n':
                       # print (filename)
                        numOfLinesToRead = int(line[7:8])
                    else:
                        if line[9]=='\n':
                            numOfLinesToRead = int(line[7:9])
                        else:
                            if line[7:10].isdigit():
                                numOfLinesToRead = int(line[7:10])
                            else:
                                startread = True
                if numOfLinesToRead != 0:
                    if linecounter == totalNumberofLines-numOfLinesToRead+1:
                        #print(linecounter)
                        startread = True
                if startread:
                      buf += line


            message=buf;
            self.docs.append(Document(docid, subject, message)) # the last one
        counter = 0
        for temp in self.docs:

            if temp.docID.find("comp.graphics") != -1:
                self.class1items1.append(temp.docID)
                self.classDocumentLookup.setdefault('1', []).append(temp.docID)
            if temp.docID.find("comp.os.ms-windows.misc") != -1:
                self.class1items1.append(temp.docID)
                self.classDocumentLookup.setdefault('1', []).append(temp.docID)
            if temp.docID.find("comp.sys.ibm.pc.hardware") != -1:
                self.class1items1.append(temp.docID)
                self.classDocumentLookup.setdefault('1', []).append(temp.docID)
            if temp.docID.find("comp.sys.mac.hardware") != -1:
                self.class1items1.append(temp.docID)
                self.classDocumentLookup.setdefault('1', []).append(temp.docID)
            if temp.docID.find("comp.windows.x") != -1:
                self.class1items1.append(temp.docID)
                self.classDocumentLookup.setdefault('1', []).append(temp.docID)

            if temp.docID.find("rec.autos") != -1:
                self.class1items2.append(temp.docID)
                self.classDocumentLookup.setdefault('2', []).append(temp.docID)
            if temp.docID.find("rec.motorcycles") != -1:
                self.class1items2.append(temp.docID)
                self.classDocumentLookup.setdefault('2', []).append(temp.docID)
            if temp.docID.find("rec.sport.baseball") != -1:
                self.class1items2.append(temp.docID)
                self.classDocumentLookup.setdefault('2', []).append(temp.docID)
            if temp.docID.find("rec.sport.hockey") != -1:
                self.class1items2.append(temp.docID)
                self.classDocumentLookup.setdefault('2', []).append(temp.docID)

            if temp.docID.find("sci.crypt") != -1:
                self.class1items3.append(temp.docID)
                self.classDocumentLookup.setdefault('3', []).append(temp.docID)
            if temp.docID.find("sci.electronics") != -1:
                self.class1items3.append(temp.docID)
                self.classDocumentLookup.setdefault('3', []).append(temp.docID)
            if temp.docID.find("sci.med") != -1:
                self.class1items3.append(temp.docID)
                self.classDocumentLookup.setdefault('3', []).append(temp.docID)
            if temp.docID.find("sci.space") != -1:
                self.class1items3.append(temp.docID)
                self.classDocumentLookup.setdefault('3', []).append(temp.docID)

            if temp.docID.find("misc.forsale") != -1:
                self.class1items4.append(temp.docID)
                self.classDocumentLookup.setdefault('4', []).append(temp.docID)

            if temp.docID.find("talk.politics.misc") != -1:
                self.class1items5.append(temp.docID)

                self.classDocumentLookup.setdefault('5', []).append(temp.docID)
            if temp.docID.find("talk.politics.guns") != -1:
                self.class1items5.append(temp.docID)
                self.classDocumentLookup.setdefault('5', []).append(temp.docID)
            if temp.docID.find("talk.politics.mideast") != -1:
                self.class1items5.append(temp.docID)
                self.classDocumentLookup.setdefault('5', []).append(temp.docID)

            if temp.docID.find("talk.religion.misc") != -1:
                self.class1items6.append(temp.docID)
                self.classDocumentLookup.setdefault('6', []).append(temp.docID)
            if temp.docID.find("alt.atheism") != -1:
                self.class1items6.append(temp.docID)
                self.classDocumentLookup.setdefault('6', []).append(temp.docID)
            if temp.docID.find("soc.religion.christian") != -1:
                self.class1items6.append(temp.docID)
                self.classDocumentLookup.setdefault('6', []).append(temp.docID)
            counter = counter + 1



if __name__ == '__main__':
    ''' testing '''
    cwd = os.getcwd()+"\\mini_newsgroups"
    #print(glob.glob(cwd+"/mini_newsgroups/*.FILE"))
    dataFileslist = []

    for path, subdirs, files in os.walk(cwd):
        for name in files:
           # if fnmatch(name, pattern):
           # print(os.path.join(path, name))
            dataFileslist.append(os.path.join(path, name))
    newsGroupFile = NewsGroup (dataFileslist)
   # for doc in newsGroupFile.docs:
   #     print(doc.docID)
   #     print(doc.subject)
   #     print(doc.message)
    print(len(newsGroupFile.docs))
    print(len(newsGroupFile.class1items1))
    print(len(newsGroupFile.class1items2))
    print(len(newsGroupFile.class1items3))
    print(len(newsGroupFile.class1items4))
    print(len(newsGroupFile.class1items5))
    print(len(newsGroupFile.class1items6))

    #21884