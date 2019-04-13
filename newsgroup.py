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

        for filename in files:
            newsGroupFile = open(filename)
            head, tail = os.path.split(filename)
            docid = tail
            subject = ''
            message = ''
            startread = False
            buf = ''
            for line in newsGroupFile:
    #            print (line)

                if 'Subject:' in line:
                    subject = line[9:] # got title
                elif 'Lines:' in line:
                    startread = True
                    line=''
                if startread:
                      buf += line


            message=buf;
            self.docs.append(Document(docid, subject, message)) # the last one

            if filename.find("comp.graphics") != -1:
                self.class1items1.append(docid)
                self.classDocumentLookup.setdefault('1', []).append(docid)
            if filename.find("comp.os.ms-windows.misc") != -1:
                self.class1items1.append(docid)
                self.classDocumentLookup.setdefault('1', []).append(docid)
            if filename.find("comp.sys.ibm.pc.hardware") != -1:
                self.class1items1.append(docid)
                self.classDocumentLookup.setdefault('1', []).append(docid)
            if filename.find("comp.sys.mac.hardware") != -1:
                self.class1items1.append(docid)
                self.classDocumentLookup.setdefault('1', []).append(docid)
            if filename.find("comp.windows.x") != -1:
                self.class1items1.append(docid)
                self.classDocumentLookup.setdefault('1', []).append(docid)

            if filename.find("rec.autos") != -1:
                self.class1items2.append(docid)
                self.classDocumentLookup.setdefault('2', []).append(docid)
            if filename.find("rec.motorcycles") != -1:
                self.class1items2.append(docid)
                self.classDocumentLookup.setdefault('2', []).append(docid)
            if filename.find("rec.sport.baseball") != -1:
                self.class1items2.append(docid)
                self.classDocumentLookup.setdefault('2', []).append(docid)
            if filename.find("rec.sport.hockey") != -1:
                self.class1items2.append(docid)
                self.classDocumentLookup.setdefault('2', []).append(docid)

            if filename.find("sci.crypt") != -1:
                self.class1items3.append(docid)
                self.classDocumentLookup.setdefault('3', []).append(docid)
            if filename.find("sci.electronics") != -1:
                self.class1items3.append(docid)
                self.classDocumentLookup.setdefault('3', []).append(docid)
            if filename.find("sci.med") != -1:
                self.class1items3.append(docid)
                self.classDocumentLookup.setdefault('3', []).append(docid)
            if filename.find("sci.space") != -1:
                self.class1items3.append(docid)
                self.classDocumentLookup.setdefault('3', []).append(docid)

            if filename.find("misc.forsale") != -1:
                self.class1items4.append(docid)
                self.classDocumentLookup.setdefault('4', []).append(docid)

            if filename.find("talk.politics.misc") != -1:
                self.class1items5.append(docid)
                self.classDocumentLookup.setdefault('5', []).append(docid)
            if filename.find("talk.politics.guns") != -1:
                self.class1items5.append(docid)
                self.classDocumentLookup.setdefault('5', []).append(docid)
            if filename.find("talk.politics.mideast") != -1:
                self.class1items5.append(docid)
                self.classDocumentLookup.setdefault('5', []).append(docid)

            if filename.find("talk.religion.misc") != -1:
                self.class1items6.append(docid)
                self.classDocumentLookup.setdefault('6', []).append(docid)
            if filename.find("alt.atheism") != -1:
                self.class1items6.append(docid)
                self.classDocumentLookup.setdefault('6', []).append(docid)
            if filename.find("soc.religion.christian") != -1:
                self.class1items6.append(docid)
                self.classDocumentLookup.setdefault('6', []).append(docid)
           # self.classDocumentLookup.setdefault('1', []).append('apple')
           # self.classDocumentLookup[1] = self.class1items1
            #self.classDocumentLookup[2] = self.class1items2
          #  self.classDocumentLookup[3] = self.class1items3
            #self.classDocumentLookup[4] = self.class1items4
           # self.classDocumentLookup[5] = self.class1items5
            #self.classDocumentLookup[6] = self.class1items6



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
   # print(len(newsGroupFile.docs))
   # print(len(newsGroupFile.class1items1))
   # print(len(newsGroupFile.class1items2))
   # print(len(newsGroupFile.class1items3))
   # print(len(newsGroupFile.class1items4))
   # print(len(newsGroupFile.class1items5))
   # print(len(newsGroupFile.class1items6))

    #21884