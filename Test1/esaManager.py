#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18/3/2015

@author: ucsp
'''
from Test1.textProcesser import Comment_proccesor as CP
from Test1.textSegmentation import Segmentation as Segm
from Test1.entityManager import EManager as EM

class EntitySA(object):
    
    def __init__(self):
        pass
    
    def classify(self, comment , entidades_detectadas):
        seg = Segm(comment)
        segmentos = seg.find_sentences()
        
        em = EM()
        for i in entidades_detectadas:
            em.add_entity(i)
        
        for i in segmentos:
            for j in entidades_detectadas:
                words = i.split()
                for k in words:
                    if k == j:
                        proc = CP(i,True)
                        text = proc.get_processed_comment()
                        atributo = [i, text, "NULL"]
                        em.add_attribute(j, atributo)
        
        em.find_polarity(entidades_detectadas)  
        em.get_entity_polarity(entidades_detectadas)
        em.print_entities()
        
        
if __name__ == '__main__':
    
    p = "movistar es una pesima empresa sin embargo me gustan sus celulares"
    entidades_detectadas = ["movistar" , "empresa" , "celulares"]
    
    manager = EntitySA()
    manager.classify(p, entidades_detectadas)
    
    
    
    
    '''
    seg = Segm(p)
    segmentos = seg.find_sentences()
    em = EM()    
    
    for i in entidades_detectadas:
        em.add_entity(i)    
    print ""
        
    for i in segmentos:
        for j in entidades_detectadas:
            words = i.split()
            for k in words:
                if k == j:
                    proc = CP(i, True)
                    text = proc.get_processed_comment()
                    atributo = [i, text, "NULL"]
                    em.add_attribute(j, atributo)
    
    
    entidades = ["movistar" , "celulares", "empresa"]
    em.find_polarity(entidades)
    em.print_entities()
    
    '''
        
