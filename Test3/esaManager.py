#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 15/11/2014

@author: andoni
'''
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

from Test3.classifier import Classifier

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


if __name__ == '__main__':
    
    comments = ["esto no esta muy malo" , "esto esta muy malo :) :) :)" , "hola :( :)"]
    manager = UnSupervisedManager(comments)
    sentiment = manager.classify_comments()
    print sentiment 


