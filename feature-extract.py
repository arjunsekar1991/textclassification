from index import InvertedIndex

class FeatureExtraction:
    def __new__(cls):  # __new__ is an implicit classmethod
        self = object.__new__(cls)
        return self
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
        if typeOFFeature ==0:
            print ('start')


if __name__ == '__main__':
    fxtraction = FeatureExtraction()
    fxtraction.extractfeature('mini_newsgroups','feature_definition_file','class_definition_file','training_data_file','type_of_feature')

