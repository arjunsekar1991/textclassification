from index import InvertedIndex
import os

from newsgroup import NewsGroup
class FeatureExtraction:
    def __new__(cls):  # __new__ is an implicit classmethod
        self = object.__new__(cls)
        self.termIdLookup = {}
        return self

    def getKeysByValue(self,dictOfElements, valueToFind):
        #listOfKeys = list()
        return dictOfElements[valueToFind]
    def getNewsGroupFile(self,collectionDir):
        cwd = os.getcwd() + "\\" + collectionDir
        dataFileslist = []

        for path, subdirs, files in os.walk(cwd):
            for name in files:
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
            self.termIdLookup[x] = counter
        f.close()

        #as per the proejct requirement hardcoding the class files here and outputting
        classDefinitiontuple = ("1 comp.graphics",
                                "1 comp.os.ms-windows.misc",
                                "1 comp.sys.ibm.pc.hardware",
                                "1 comp.sys.mac.hardware",
                                "1 comp.windows.x",
                                "2 rec.autos",
                                "2 rec.motorcycles",
                                "2 rec.sport.baseball",
                                "2 rec.sport.hockey",
                                "3 sci.crypt",
                                "3 sci.electronics",
                                "3 sci.med",
                                "3 sci.space",
                                "4 misc.forsale",
                                "5 talk.politics.misc",
                                "5 talk.politics.guns",
                                "5 talk.politics.mideast",
                                "6 talk.religion.misc",
                                "6 alt.atheism",
                                "6 soc.religion.christian")

        classfile = open(classDefinitionFile, "w")
        for x in classDefinitiontuple:
            classfile.write(x+"\n")
        classfile.close()
        #end of hardcoded class files

        print('tf start')
        libsvmtf = {}

        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)


        for x in invertedIndex.items.keys():

            for postingobject in invertedIndex.items.get(x).posting.keys():
                #libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID,[]).append(self.getKeysByValue(self.termIdLookup,x))
                #libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID,[]).append(invertedIndex.items.get(x).posting.get(postingobject).termfreq)
               # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')

        for x in libsvmtf:
            tfdata =''
            libsvmtffile = open("training_data_file.TF", "a")
            if x in newsgroup.class1items1:
                classid = 1
            if x in newsgroup.class1items2:
                classid = 2
            if x in newsgroup.class1items3:
                classid = 3
            if x in newsgroup.class1items4:
                classid = 4
            if x in newsgroup.class1items5:
                classid = 5
            if x in newsgroup.class1items6:
                classid = 6
        #    print('\t '.join(libsvmtf))
            #tfdata = str(x) +" : "+str(''.join(str(libsvmtf[x]).split(",")))[1:-1] + "\n"


        #        for row in reader:  # read a row as {column1: value1, column2: value2,...}
         #           for (k, v) in row.items():  # go over each column name and value
         #               columns[k].append(v)  # append the value into the appropriate list

            #     saved_column = df.column_name  # you can also use df['column_name']
            tfdata = str(classid) + " " + str(''.join(str(libsvmtf[x]).split(",")))[1:-1] + "\n"
           # print (tfdata)
            libsvmtffile.write(tfdata)
        libsvmtffile.close()

        print('tf complete')

        print('idf start')
        libsvmidf = {}
        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)

        for x in invertedIndex.items.keys():

            for postingobject in invertedIndex.items.get(x).posting.keys():
                # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(
                    self.getKeysByValue(self.termIdLookup, x))
                # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(
                    invertedIndex.items.get(x).idf)
            # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')

        for x in libsvmidf:
            idfdata = ''
            libsvmidffile = open("training_data_file.IDF", "a")
            if x in newsgroup.class1items1:
                classid = 1
            if x in newsgroup.class1items2:
                classid = 2
            if x in newsgroup.class1items3:
                classid = 3
            if x in newsgroup.class1items4:
                classid = 4
            if x in newsgroup.class1items5:
                classid = 5
            if x in newsgroup.class1items6:
                classid = 6
            #    print('\t '.join(libsvmtf))
            # tfdata = str(x) +" : "+str(''.join(str(libsvmtf[x]).split(",")))[1:-1] + "\n"

            #        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            #           for (k, v) in row.items():  # go over each column name and value
            #               columns[k].append(v)  # append the value into the appropriate list

            #     saved_column = df.column_name  # you can also use df['column_name']
            idfdata = str(classid) + " " + str(''.join(str(libsvmidf[x]).split(",")))[1:-1] + "\n"
            print(idfdata)
            libsvmidffile.write(idfdata)
        libsvmidffile.close()

        print('idf complete')

        print('TF-idf start')
        libsvmtfidf = {}
        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)

        for x in invertedIndex.items.keys():

            for postingobject in invertedIndex.items.get(x).posting.keys():
                # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmtfidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(
                    self.getKeysByValue(self.termIdLookup, x))
                # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmtfidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(
                    invertedIndex.items.get(x).posting.get(postingobject).termfreq*invertedIndex.items.get(x).idf)
            # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')

        for x in libsvmtfidf:
            tfidfdata = ''
            libsvmtfidffile = open("training_data_file.TFIDF", "a")
            if x in newsgroup.class1items1:
                classid = 1
            if x in newsgroup.class1items2:
                classid = 2
            if x in newsgroup.class1items3:
                classid = 3
            if x in newsgroup.class1items4:
                classid = 4
            if x in newsgroup.class1items5:
                classid = 5
            if x in newsgroup.class1items6:
                classid = 6
            #    print('\t '.join(libsvmtf))
            # tfdata = str(x) +" : "+str(''.join(str(libsvmtf[x]).split(",")))[1:-1] + "\n"

            #        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            #           for (k, v) in row.items():  # go over each column name and value
            #               columns[k].append(v)  # append the value into the appropriate list

            #     saved_column = df.column_name  # you can also use df['column_name']
            tfidfdata = str(classid) + " " + str(''.join(str(libsvmtfidf[x]).split(",")))[1:-1] + "\n"
            print(tfidfdata)
            libsvmtfidffile.write(tfidfdata)
        libsvmtfidffile.close()

        print('TF-idf complete')

#training_data_file.TF, training_data_file.IDF, and training_data_file.TFIDF



if __name__ == '__main__':
    fxtraction = FeatureExtraction()
    fxtraction.extractfeature('mini_newsgroups','feature_definition_file','class_definition_file','training_data_file',0)

