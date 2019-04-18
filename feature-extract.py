from index import InvertedIndex
import os
import string
import sys
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
        cwd = collectionDir
        dataFileslist = []

        for path, subdirs, files in os.walk(cwd):
            for name in files:
                dataFileslist.append(os.path.join(path, name))
        newsGroupFile = NewsGroup(dataFileslist)
        return newsGroupFile

    def extractfeature( self,directoryOfNewsgroup, featureDefinitionFile,classDefinitionFile,trainingDataFile):
        iindexObject = InvertedIndex()
        invertedIndex = iindexObject.indexingCranfield(directoryOfNewsgroup)
        if os.path.exists(featureDefinitionFile):
            os.remove(featureDefinitionFile)
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
        if os.path.exists(classDefinitionFile):
            os.remove(classDefinitionFile)
        classfile = open(classDefinitionFile, "w")
        for x in classDefinitiontuple:
            classfile.write(x+"\n")
        classfile.close()
        #end of hardcoded class files

     #   print('tf start')
        libsvmtf = {}
        if os.path.exists(trainingDataFile+".TF"):
            os.remove(trainingDataFile+".TF")
        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)


        for x in invertedIndex.items.keys():

            for postingobject in invertedIndex.items.get(x).posting.keys():
                #libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID,[]).append(self.getKeysByValue(self.termIdLookup,x))
                libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(':')
                #libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID,[]).append(round(invertedIndex.items.get(x).posting.get(postingobject).termfreq,5))
               # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')

        for x in libsvmtf:
            tfdata =''
            libsvmtffile = open(trainingDataFile+".TF", "a")
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

            #print (str(tempstr).split("'",""))
            tfdata = str(classid) + " " + str(''.join(str(libsvmtf[x]).split(",")))[1:-1] + "\n"
            tfdata = str.replace(tfdata, " ':' ", ":")
       #     print (tfdata)
            libsvmtffile.write(tfdata)
        libsvmtffile.close()

      #  print('tf complete')

    #    print('idf start')
        libsvmidf = {}
        if os.path.exists(trainingDataFile+".IDF"):
            os.remove(trainingDataFile+".IDF")
        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)

        for x in invertedIndex.items.keys():

            for postingobject in invertedIndex.items.get(x).posting.keys():
                # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(
                    self.getKeysByValue(self.termIdLookup, x))
                libsvmidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(':')
                # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(
                    invertedIndex.items.get(x).idf)
            # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')

        for x in libsvmidf:
            idfdata = ''
            libsvmidffile = open(trainingDataFile+".IDF", "a")
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
            idfdata = str.replace(idfdata, " ':' ", ":")
           # print(idfdata)
            libsvmidffile.write(idfdata)
        libsvmidffile.close()

     #   print('idf complete')

      #  print('TF-idf start')
        libsvmtfidf = {}
        if os.path.exists(trainingDataFile+".TFIDF"):
            os.remove(trainingDataFile+".TFIDF")
        newsgroup = self.getNewsGroupFile(directoryOfNewsgroup)

        for x in invertedIndex.items.keys():

            for postingobject in invertedIndex.items.get(x).posting.keys():
                # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmtfidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(
                    self.getKeysByValue(self.termIdLookup, x))
                libsvmtfidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(':')
                # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')
                libsvmtfidf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append(
                    invertedIndex.items.get(x).posting.get(postingobject).termfreq*invertedIndex.items.get(x).idf)
            # libsvmtf.setdefault(invertedIndex.items.get(x).posting.get(postingobject).docID, []).append('\t')

        for x in libsvmtfidf:
            tfidfdata = ''
            libsvmtfidffile = open(trainingDataFile+".TFIDF", "a")
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
            tfidfdata = str.replace(tfidfdata, " ':' ", ":")
           # print(tfidfdata)
            libsvmtfidffile.write(tfidfdata)
        libsvmtfidffile.close()

       # print('TF-idf complete')

#training_data_file.TF, training_data_file.IDF, and training_data_file.TFIDF


def test():
    ''' test your code thoroughly. put the testing cases here'''
    print('Start of testing')

    try:
        #statinfo = os.stat("trainingDataFile.TF")
        # here we are compaing the file should have
        trainingDatafileTf = open(str(sys.argv[4])+".TF")
        linecounter = 0
        for line in trainingDatafileTf:
            # print (line)
            linecounter = linecounter + 1

        if linecounter == 2000:
            print('trainingDataFile.TF generated successfully')
        else:
            print('trainingDataFile.TF is screwed')
    except:
        print('trainingDataFile.TF is screwed')
        sys.exit()

    try:
        # statinfo = os.stat("trainingDataFile.TF")
        # here we are compaing the file should have
        trainingDatafileidf = open(str(sys.argv[4])+".IDF")
        linecounter = 0
        for line in trainingDatafileidf:
            # print (line)
            linecounter = linecounter + 1

        if linecounter == 2000:
            print('training_data_file.IDF generated successfully')
        else:
            print('training_data_file.IDF is screwed')
    except:
        print('training_data_file.IDF is screwed')
        sys.exit()

    try:
        # statinfo = os.stat("trainingDataFile.TF")
        # here we are compaing the file should have
        trainingDatafileTfIDF = open(str(sys.argv[4])+".TFIDF")
        linecounter = 0
        for line in trainingDatafileTfIDF:
            # print (line)
            linecounter = linecounter + 1

        if linecounter == 2000:
            print('training_data_file.TFIDF generated successfully')
        else:
            print('training_data_file.TFIDF is screwed')
    except:
        print('training_data_file.TFIDF is screwed')
        sys.exit()

#6 1:2 2:5 3:1 4:9 5:1 6:1 7:4 8:5 9:1 10:1 11:1 12:1 13:2 14:1 15:2 16:1 17:1 18:1 19:1 20:3 21:2 22:6 23:1 24:2 25:1 26:1 27:2 28:1 29:5 30:2 31:1 32:2 33:1 34:1 35:1 36:1 37:1 38:1 39:1 40:2 41:1 42:1 43:1 44:1 45:1 46:1 47:1 48:1 49:1 50:1 51:1 52:1 53:1 54:1 55:1 56:1 57:1 58:1 59:1 60:1 61:1 62:2 63:1 64:1 65:1 66:1 67:1 68:1 69:1 70:1 71:1 72:1 73:1 74:1 75:1 76:1 77:1 78:1 79:1
    try:
        #statinfo = os.stat("trainingDataFile.TF")
        # here we are compaing the file should have
        trainingDatafileTf = open(str(sys.argv[4])+".TF")
        linecounter = 0
        for line in trainingDatafileTf:
            # print (line)
            linecounter = linecounter + 1

            if linecounter == 1:

                if line == "6 1:2 2:5 3:1 4:9 5:1 6:1 7:4 8:5 9:1 10:1 11:1 12:1 13:2 14:1 15:2 16:1 17:1 18:1 19:1 20:3 21:2 22:6 23:1 24:2 25:1 26:1 27:2 28:1 29:5 30:2 31:1 32:2 33:1 34:1 35:1 36:1 37:1 38:1 39:1 40:2 41:1 42:1 43:1 44:1 45:1 46:1 47:1 48:1 49:1 50:1 51:1 52:1 53:1 54:1 55:1 56:1 57:1 58:1 59:1 60:1 61:1 62:2 63:1 64:1 65:1 66:1 67:1 68:1 69:1 70:1 71:1 72:1 73:1 74:1 75:1 76:1 77:1 78:1 79:1\n":
                    print('trainingDataFile.TF contents are correct')

                else:
                    print('trainingDataFile.TF contents are  screwed')
    except:
        print('trainingDataFile.TF is screwed')
        sys.exit()

    try:
        # statinfo = os.stat("trainingDataFile.TF")
        # here we are compaing the file should have
        trainingDatafileIDF = open(str(sys.argv[4])+".IDF")
        linecounter = 0
        for line in trainingDatafileIDF:
            # print (line)
            linecounter = linecounter + 1

            if linecounter == 1:

                if line == "6 1:0.06600683616875773 2:0.8401321529074333 3:2.823908740944318 4:0.024568191490737024 5:1.886056647693163 6:1.5686362358410126 7:0.012110390002254631 8:0.831207979685818 9:0.33960890159753293 10:2.9999999999999996 11:2.5228787452803374 12:1.838631997765025 13:1.7099653886374817 14:1.8696662315049937 15:2.455931955649724 16:0.28777133038046465 17:0.34872198600185594 18:0.3032069149182557 19:3.301029995663981 20:0.09312646527792955 21:3.301029995663981 22:0.19928292171761497 23:2.9999999999999996 24:0.07288638806623948 25:1.6289321377282635 26:2.9999999999999996 27:0.07032568205141217 28:0.269621531412357 29:0.7189666327522723 30:0.8431480989299888 31:1.0222763947111522 32:1.6289321377282635 33:1.9208187539523751 34:2.045757490560675 35:1.4145392704914992 36:1.346787486224656 37:1.6989700043360185 38:0.22475374025976355 39:1.6108339156354674 40:0.8401321529074333 41:1.2111248842245832 42:1.6989700043360185 43:1.314258261397736 44:2.259637310505756 45:0.4359260210228532 46:2.6989700043360183 47:1.5086383061657274 48:2.602059991327962 49:1.0530567293021746 50:1.9586073148417746 51:0.8181564120552274 52:1.1643094285075744 53:1.0861861476162833 54:3.301029995663981 55:1.7825160557860937 56:2.602059991327962 57:1.5301779840218368 58:1.7825160557860937 59:0.16877030613293661 60:0.24184537803261 61:1.886056647693163 62:2.823908740944318 63:2.301029995663981 64:2.9999999999999996 65:2.9999999999999996 66:1.6989700043360185 67:1.3279021420642825 68:1.4749551929631548 69:1.4436974992327125 70:2.5228787452803374 71:2.455931955649724 72:1.5686362358410126 73:2.045757490560675 74:1.3233063903751332 75:2.9999999999999996 76:2.9999999999999996 77:2.0969100130080562 78:1.7958800173440752 79:2.9999999999999996\n":
                    print('training_data_file.IDF contents are correct')

                else:
                    print('training_data_file.IDF contents are  screwed')
    except:
        print('training_data_file.IDF is screwed')
        sys.exit()

    try:
        # statinfo = os.stat("trainingDataFile.TF")
        # here we are compaing the file should have
        trainingDatafileTfIDF = open(str(sys.argv[4])+".TFIDF")
        linecounter = 0
        for line in trainingDatafileTfIDF:
            # print (line)
            linecounter = linecounter + 1

            if linecounter == 1:

                if line == "6 1:0.13201367233751546 2:4.200660764537166 3:2.823908740944318 4:0.2211137234166332 5:1.886056647693163 6:1.5686362358410126 7:0.048441560009018524 8:4.15603989842909 9:0.33960890159753293 10:2.9999999999999996 11:2.5228787452803374 12:1.838631997765025 13:3.4199307772749634 14:1.8696662315049937 15:4.911863911299448 16:0.28777133038046465 17:0.34872198600185594 18:0.3032069149182557 19:3.301029995663981 20:0.2793793958337886 21:6.602059991327962 22:1.1956975303056898 23:2.9999999999999996 24:0.14577277613247897 25:1.6289321377282635 26:2.9999999999999996 27:0.14065136410282433 28:0.269621531412357 29:3.5948331637613617 30:1.6862961978599775 31:1.0222763947111522 32:3.257864275456527 33:1.9208187539523751 34:2.045757490560675 35:1.4145392704914992 36:1.346787486224656 37:1.6989700043360185 38:0.22475374025976355 39:1.6108339156354674 40:1.6802643058148665 41:1.2111248842245832 42:1.6989700043360185 43:1.314258261397736 44:2.259637310505756 45:0.4359260210228532 46:2.6989700043360183 47:1.5086383061657274 48:2.602059991327962 49:1.0530567293021746 50:1.9586073148417746 51:0.8181564120552274 52:1.1643094285075744 53:1.0861861476162833 54:3.301029995663981 55:1.7825160557860937 56:2.602059991327962 57:1.5301779840218368 58:1.7825160557860937 59:0.16877030613293661 60:0.24184537803261 61:1.886056647693163 62:5.647817481888636 63:2.301029995663981 64:2.9999999999999996 65:2.9999999999999996 66:1.6989700043360185 67:1.3279021420642825 68:1.4749551929631548 69:1.4436974992327125 70:2.5228787452803374 71:2.455931955649724 72:1.5686362358410126 73:2.045757490560675 74:1.3233063903751332 75:2.9999999999999996 76:2.9999999999999996 77:2.0969100130080562 78:1.7958800173440752 79:2.9999999999999996\n":
                    print('training_data_file.TFIDF contents are correct')

                else:
                    print('training_data_file.TFIDF contents are  screwed')
    except:
        print('training_data_file.TFIDF is screwed')
        sys.exit()

    try:
        iindexObject = InvertedIndex()
        invertedIndex = iindexObject.indexingCranfield(str(sys.argv[1]))
        if invertedIndex.nDocs == 2000:
            print("Inverted index is correct")
        else:
            print ("Inverted index is screwed")
    except:
        print('Inverted Index is screwed')
        sys.exit()

    try:
        # statinfo = os.stat("trainingDataFile.TF")
        # here we are compaing the file should have
        classDefinitionFile = open(str(sys.argv[3]))
        linecounter = 0
        for line in classDefinitionFile:
            # print (line)
            linecounter = linecounter + 1

        if linecounter == 20:
            print('classDefinitionFile contents are correct')

        else:
            print('classDefinitionFile contents are  screwed')
    except:
        print('classDefinitionFile contents are screwed')
        sys.exit()
    print("Testing completed successfully")

if __name__ == '__main__':
    fxtraction = FeatureExtraction()
    fxtraction.extractfeature(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4]))

    # Testing after feature extraction is done
    test()

    #fxtraction.extractfeature('mini_newsgroups','feature_definition_file','class_definition_file','training_data_file')
