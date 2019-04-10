'''
Index structure:
    The Index class contains a list of IndexItems, stored in a dictionary type for easier access
    each IndexItem contains the term and a set of PostingItems
    each PostingItem contains a document ID and a list of positions that the term occurs
'''

import re
import os
from newsgroup import NewsGroup
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
import json, codecs
import numpy as np
import math
from nltk.corpus import stopwords
import jsonpickle
import string
import sys
class Posting:
    def __init__(self, docID):
        self.docID = docID
        self.positions = []
        self.termfreq = 0;

    def append(self, pos):
        self.positions.append(pos)
         #adding term frequency here
        self.termfreq  = self.termfreq+1;
    def sort(self):
        ''' sort positions'''
        self.positions.sort()

    def merge(self, positions):
        self.positions.extend(positions)
        #this will add the term frequency of the merged posting with existing posting . helpful during merging same terms after preprocessing
        self.termfreq = self.termfreq + positions.length

    def term_freq(self):
        ''' return the term frequency in the document'''
        return self.termfreq



class IndexItem:
    def __init__(self, term):
        self.term = term
        self.posting = {}  # postings are stored in a python dict for easier index building
        self.idf = 0
        self.tf = 0
        #self.sorted_posting s= [] # may sort them by docID for easier query processing

    def add(self, docid, pos):
        ''' add a posting'''
        if docid not in self.posting:
            self.posting[docid] = Posting(docid)
        self.posting[docid].append(pos)

    def sort(self):
        ''' sort by document ID for more efficient merging. For each document also sort the positions'''
        # ToDo
        #


class InvertedIndex:

    def __init__(self):
        self.items = {} # list of IndexItems
        self.nDocs = 0  # the number of indexed documents


    def indexDoc(self, doc): # indexing a Document object
        ''' indexing a docuemnt, using the simple SPIMI algorithm, but no need to store blocks due to the small collection we are handling. Using save/load the whole index instead'''

        # ToDo: indexing only title and body; use some functions defined in util.py
        # (1) convert to lower cases,
        # (2) remove stopwords,
        # (3) stemming
        # after applying step1  there are 12236 items
        # after applying step3  there are 9666 items
        # after applying step2  there are 9567 items
        self.nDocs = self.nDocs + 1;
        titletoken = word_tokenize(doc.subject)
        bodytoken = word_tokenize(doc.message)
#        titletoken = re.split(" ", doc.title.replace('\n', ' '))
#        titletoken = ' '.join(titletoken).split()
#        bodytoken = re.split(" ", doc.body.replace('\n', ' '))
#        bodytoken = ' '.join(bodytoken).split()
        tokens = titletoken + bodytoken
        tokens = [element.lower() for element in tokens];

        stop_words = set(stopwords.words('english'))
       # for i in tokens :
      #      if i in stop_words:

  #              print("key delete works")
     #           tokens.remove(i)
        k = 0
        positionindoc = 1
        while k < len(tokens):

                tempindexitem = IndexItem(tokens[k])

                #

                #stemming comes here
                ps = PorterStemmer()
             #   punctuation = "()/\\"
             #   tokens[k] = "".join([ch for ch in tokens[k] if ch not in punctuation])
                stemmedToken = ps.stem(tokens[k])

                if (stemmedToken in self.items ):
                    self.items.get(stemmedToken).add(doc.docID, positionindoc)

                else:
                    tempindexitem.add(doc.docID, positionindoc)
                    self.items[stemmedToken] = tempindexitem

                positionindoc = positionindoc + len(tokens[k]) + 1;

                k = k + 1

    def sort(self):
        ''' sort all posting lists by docID'''
        # ToDo
        # while creating postings i created them in the order sorted by doc id hence not doing anything here

    def find(self, term):
        return self.items[term]

    def save(self, filename):
        ''' save to disk'''
        # ToDo: using your preferred method to serialize/deserialize the index
        jsonEncoded = jsonpickle.encode(self)
  #      print(jsonEncoded)
        fh = open(filename, 'a')
        fh.write(jsonEncoded)
        #fh.close

    def load(self, filename):
        ''' load from disk'''
        # ToDo

        f = open(filename, "r")
        jsonString = f.read()
#        print(jsonString)
        self = jsonpickle.decode(jsonString)
#        print(self.items.keys().__len__())
        return self

    def idf(self, term):
        ''' compute the inverted document frequency for a given term'''
        # ToDo: return the IDF of the term
        rawvalue = self.nDocs/(len(list(self.items[term].posting.keys())))
        self.items[term].idf = math.log(rawvalue,10)

    def tf(self, term):
        for x in self.items[term].posting:
            self.items[term].tf = self.items[term].tf +self.items[term].posting[x].termfreq
        self.items[term].tf = self.items[term].tf /len(self.items[term].posting)

    # more methods if needed


    def test(self):
        ''' test your code thoroughly. put the testing cases here'''
        print('Pass')


    def indexingCranfield(self,collectionDir):
        # ToDo: indexing the Cranfield dataset and save the index to a file
        # command line usage: "python index.py cran.all index_file"
        # the index is saved to index_file
        cwd = os.getcwd() + "\\"+collectionDir
        # print(glob.glob(cwd+"/mini_newsgroups/*.FILE"))
        dataFileslist = []

        for path, subdirs, files in os.walk(cwd):
            for name in files:
                # if fnmatch(name, pattern):
                # print(os.path.join(path, name))
                dataFileslist.append(os.path.join(path, name))
        newsGroupFile = NewsGroup(dataFileslist)
        iindex = InvertedIndex()
        for doc in newsGroupFile.docs:
            iindex.indexDoc(doc)
        # doing  stop word removal here ?
        #with open("stopwords") as f:
        #    for line in f:
        #        if line.strip() in iindex.items:
        #            del iindex.items[line.strip()]
        # Do something with 'line'
        stop_words = set(stopwords.words('english'))
     #   print(len(iindex.items))
        for terms in list(iindex.items.keys()):
            #        print(terms)
            if terms in stop_words:
              #  print("key delete works")
                del iindex.items[terms]
        for terms in iindex.items:
    #        print(terms)
            iindex.idf(terms)
        for terms in iindex.items:
            #        print(terms)
            iindex.tf(terms)

        # iindex.save(indexfilename)
        print(len(iindex.items))
        print("Index builded successfully")
        return iindex

#42673

if __name__ == '__main__':
    # test()
   # indexingCranfield((str(sys.argv[1]), str(sys.argv[2]))
    ii = InvertedIndex()
    ii.indexingCranfield('mini_newsgroups')

#idf log(number of documents/total number of documents term occurs)
# number of times the term occurs in particular document