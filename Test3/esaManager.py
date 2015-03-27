#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 15/11/2014

@author: andoni
'''
import sys  
reload(sys)  
#sys.setdefaultencoding('utf8')

from Test3.commentPreprocessor import Comment_proccesor as CP 
from Test3.classifier import Classifier
from Test3.textSegmentation import Segmentation as Segm 
from Test3.entityManager import EManager as EM 

class UnSupervisedManager(object):
    
    def __init__(self , comments=""):
        self.__comments = comments
    
    def classify_comments(self):
        labels = []
        obj = Classifier()
        for i in self.__comments:
            obj.classify(i)
            sentiment = obj.get_label()
            labels.append(sentiment)
        return labels

class SAClassifier(object):
    
    def __init__(self):
        pass 
    
    def classify(self, comment):
        obj = Classifier()
        obj.classify(comment)
        sentiment = obj.get_label()
        return sentiment
    
class EntitySA(object):
    
    def __init__(self):
        pass
    
    def classify(self, comment, entidades_detectadas):
        seg = Segm(comment)
        segmentos = seg.find_sentences()
        
        em = EM()
        em.add_entities(entidades_detectadas)
        
        manager = SAClassifier()
        
        for i in segmentos:
            proc = CP(i)
            texto_sin_signos = proc.remove_punctuation(i)            
            for j in entidades_detectadas:
                words = texto_sin_signos.split()
                for k in words:
                    if k==j:
                        polaridad = manager.classify(i)
                        em.add_atributte(j, i, polaridad)
                        print j + ": "  + polaridad
                         
if __name__ == '__main__':
    
    entidades_detectadas = ["movistar" , "empresa" , "claro"]
    comment = "movistar es una pesima empresa , claro es mucho mejor"


