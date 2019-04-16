from sklearn.datasets import load_svmlight_file
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import warnings
warnings.filterwarnings('ignore')
clf = MultinomialNB()
feature_vectors, targets = load_svmlight_file("training_data_file.TF")
scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')
print("MultinomialNB Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

clf2 = BernoulliNB()
feature_vectors2, targets2 = load_svmlight_file("training_data_file.IDF")
scores = cross_val_score(clf2, feature_vectors2, targets2, cv=5, scoring='f1_macro')
print("BernoulliNB Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

clf3 = KNeighborsClassifier()
feature_vectors3, targets3 = load_svmlight_file("training_data_file.TFIDF")
scores = cross_val_score(clf3, feature_vectors3, targets3, cv=5, scoring='f1_macro')
print("KNeighborsClassifier Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

clf4 = SVC(gamma='auto')
feature_vectors4, targets4 = load_svmlight_file("training_data_file.TFIDF")
scores = cross_val_score(clf4, feature_vectors4, targets4, cv=5, scoring='f1_macro')
print("SVC Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
