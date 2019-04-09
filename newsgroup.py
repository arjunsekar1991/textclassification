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

if __name__ == '__main__':
    ''' testing '''
    cwd = os.getcwd()+"\\mini_newsgroups"
    #print(glob.glob(cwd+"/mini_newsgroups/*.FILE"))
    dataFileslist = []

    for path, subdirs, files in os.walk(cwd):
        for name in files:
           # if fnmatch(name, pattern):
            print(os.path.join(path, name))
            dataFileslist.append(os.path.join(path, name))
    newsGroupFile = NewsGroup (dataFileslist)
   # for doc in newsGroupFile.docs:
    #    print(doc.docID)
     #   print(doc.subject)
      #  print(doc.message)
    print(len(newsGroupFile.docs))