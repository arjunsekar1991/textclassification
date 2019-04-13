from index import InvertedIndex
import os

from newsgroup import NewsGroup
class FeatureExtraction:
    def __new__(cls):  # __new__ is an implicit classmethod
        self = object.__new__(cls)
       # self.libsvmtf = {}
        return self
    def getNewsGroupFile(self,collectionDir):
        cwd = os.getcwd() + "\\" + collectionDir
        # print(glob.glob(cwd+"/mini_newsgroups/*.FILE"))
        dataFileslist = []

        for path, subdirs, files in os.walk(cwd):
            for name in files:
                # if fnmatch(name, pattern):
                # print(os.path.join(path, name))
                dataFileslist.append(os.path.join(path, name))
        newsGroupFile = NewsGroup(dataFileslist)
        return newsGroupFile

    def extractfeature( self,directoryOfNewsgroup, featureDefinitionFile,classDefinitionFile,trainingDataFile,typeOFFeature):
        iindexObject = InvertedIndex()
        invertedIndex = iindexObject.indexingCranfield(directoryOfNewsgroup)
        f = open(featureDefinitionFile, "w")
        counter = 0
        for x in invertedIndex.items.keys():
            counter = counter+1
            formattedData = str(counter) + " " + x + "\n"
            f.write(formattedData)
        f.close()

        #as per the proejct requirement hardcoding the class files here and outputting
        classDefinitiontuple = ("1 comp.graphics", "1 comp.os.ms-windows.misc", "1 comp.sys.ibm.pc.hardware", "1 comp.sys.mac.hardware", "1 comp.windows.x"
                                     "2 rec.autos", "2 rec.motorcycles", "2 rec.sport.baseball", "2 rec.sport.hockey"
                                     "3 sci.crypt", "3 sci.electronics", "3 sci.med", "3 sci.space",
                                     "4 misc.forsale",
                                     "5 talk.politics.misc","5 talk.politics.guns", "5 talk.politics.mideast"
                                     "6 talk.religion.misc","6 alt.atheism", "6 soc.religion.christian"

                                     )

        classfile = open(classDefinitionFile, "w")
        for x in classDefinitiontuple:
            classfile.write(x+"\n")
        classfile.close()
        #end of hardcoded class files

        print('tf start')
        libsvmtf = {}

        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)
        for tempDocName in  newsgroup.docs:
            print(tempDocName.docID)
        for x in invertedIndex.items.keys():
            for postingobject in invertedIndex.items.get(x).posting.keys():
              #  print(x)
               # print(invertedIndex.items.get(x).posting.get(postingobject).docID)
               # print(invertedIndex.items.get(x).posting.get(postingobject).termfreq)
                libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID,[]).append(x)
                libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID,[]).append(invertedIndex.items.get(x).posting.get(postingobject).termfreq)
                    #self.classDocumentLookup.setdefault('1', []).append(docid)
        print('tf complete')

        print('idf start')
        libsvmidf = {}

        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)
        for tempDocName in newsgroup.docs:
            print(tempDocName.docID)
        for x in invertedIndex.items.keys():
            for postingobject in invertedIndex.items.get(x).posting.keys():
              #  print(x)
              #  print(invertedIndex.items.get(x).posting.get(postingobject).docID)
              #  print(invertedIndex.items.get(x).posting.get(postingobject).termfreq)
                libsvmidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(x)
                libsvmidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(invertedIndex.items.get(x).idf)
                # self.classDocumentLookup.setdefault('1', []).append(docid)
        print('idf complete')

        print('TF-idf start')
        libsvmtfidf = {}

        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)
        for tempDocName in newsgroup.docs:
            print(tempDocName.docID)
        for x in invertedIndex.items.keys():
            for postingobject in invertedIndex.items.get(x).posting.keys():
              #  print(x)
               # print(invertedIndex.items.get(x).posting.get(postingobject).docID)
               # print(invertedIndex.items.get(x).posting.get(postingobject).termfreq)
                libsvmtfidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(x)
                libsvmtfidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(
                    invertedIndex.items.get(x).posting.get(postingobject).termfreq*invertedIndex.items.get(x).idf)
                # self.classDocumentLookup.setdefault('1', []).append(docid)
        print('TF-idf complete')

#training_data_file.TF, training_data_file.IDF, and training_data_file.TFIDF



if __name__ == '__main__':
    fxtraction = FeatureExtraction()
    fxtraction.extractfeature('mini_newsgroups','feature_definition_file','class_definition_file','training_data_file',0)

