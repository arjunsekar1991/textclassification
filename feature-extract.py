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
        iindex = InvertedIndex()
        invertedIndex = iindex.indexingCranfield(directoryOfNewsgroup)
        f = open(featureDefinitionFile, "w")
        counter = 0
        for x in invertedIndex.items.keys():
            counter = counter+1
            formattedData = str(counter) + " " + x + "\n"
            f.write(formattedData)
        f.close()


        print('tf start')
        libsvmtf = {}

        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)
        for tempDocName in  newsgroup.docs:
            print(tempDocName.docID)
        for x in invertedIndex.items.keys():
            for postingobject in invertedIndex.items.get(x).posting.keys():
                print(x)
                print(invertedIndex.items.get(x).posting.get(postingobject).docID)
                print(invertedIndex.items.get(x).posting.get(postingobject).termfreq)
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
                print(x)
                print(invertedIndex.items.get(x).posting.get(postingobject).docID)
                print(invertedIndex.items.get(x).posting.get(postingobject).termfreq)
                libsvmidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(x)
                libsvmidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(invertedIndex.items.get(x).idf)
                # self.classDocumentLookup.setdefault('1', []).append(docid)
        print('idf complete')





if __name__ == '__main__':
    fxtraction = FeatureExtraction()
    fxtraction.extractfeature('mini_newsgroups','feature_definition_file','class_definition_file','training_data_file',0)

