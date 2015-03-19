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
            proc = CP(i,True)            
            texto_sin_signos = proc.remove_punctuation(i)
            for j in entidades_detectadas:
                words = texto_sin_signos.split()
                for k in words:
                    if k == j:                        
                        text = proc.get_processed_comment()
                        negation = proc.has_negation()
                        print text
                        print negation
                        atributo = [i, text, negation , "NULL"]
                        print atributo
                        em.add_attribute(j, atributo)
        
        em.find_polarity(entidades_detectadas)  
        em.get_entity_polarity(entidades_detectadas)
        em.print_entities()
        
        
if __name__ == '__main__':
    
    p = "El Barza en 7 dias ha quedado fuera de la lucha por los titulos. Hacen falta cambios tanto en la plantilla como en el estilo"
    #p = "movistar es una pesima empresa sin embargo me gustan sus celulares"
    entidades_detectadas = ["Barza" , "titulos" , "plantilla"]
    #entidades_detectadas = ["movistar" , "empresa" , "celulares"]
    
    manager = EntitySA()
    manager.classify(p, entidades_detectadas)
    
        
