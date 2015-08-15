'''
Created on 15/8/2015

@author: andoni
'''
from Test4.xmlReader import Reader

simpleVectorizer = "Models/simpleVectorizer.pk1"
tfidfModel = "Models/tfidfModel.pk1"
tfidfVectorizer = "Models/tfidfVectorizer.pk1"

SVM = "Classifiers/SVM.pk1"
NB = "Classifiers/NB.pk1"
ME = "Classifiers/ME.pk1"
DT = "Classifiers/DT.pk1"




xml = "stompol-tweets-train-tagged.xml"

class SentimentManager(object):
    
    def __init__(self):
        pass
    
    def trainClassifiers(self, xml_file): 
        obj = Reader(xml_file, 1)
        for i in obj.read():
            print i 


if __name__ == '__main__':
    
    obj = SentimentManager()
    obj.trainClassifiers(xml)
    