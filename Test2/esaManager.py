#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 23/3/2015
@author: ucsp
'''

from Test2.textProcesser import Comment_proccesor as CP
from Test2.textSegmentation import Segmentation as Segm
from Test2.entityManager import EManager as EM  

class EntitySA(object):
    
    def __init__(self):
        pass 
    
    def classify(self, comment, entidades_detectadas):
        seg = Segm(comment)
        segmentos = seg.find_sentences()
        
        em = EM()
        em.add_entities(entidades_detectadas)
        
        valores = []
        
        for i in segmentos:
            proc = CP(i, True)
            texto_sin_signos = proc.remove_punctuation(i)
            print texto_sin_signos
            for j in entidades_detectadas:
                words = texto_sin_signos.split()
                for k in words:
                    if k==j:
                        texto = proc.get_processed_comment()
                        negation = proc.has_negation()
                        polaridad = em.find_polarity(texto, negation)
                        em.add_atributte(j, i, polaridad)
                        print polaridad
                        print j + ": " + em.polarity_rule(polaridad)
                                                
if __name__ == '__main__':
    
    entidades_detectadas = ["Barcelona" , "Pinto" , "RealMadrid" , "Benzema"]
    #comment = "movistar es una pesima empresa , claro es mucho mejor"
    #comment = "El Barza en 7 dias ha quedado fuera de la lucha por los titulos. Hacen falta cambios tanto en la plantilla como en el estilo"
    #comment = "movistar es una pesima empresa sin embargo me gustan sus celulares"
    #comment = "Siendo un defensor del trabajo de Mourinho, no dejo de admirar la naturalidad en la victoria de un tecnico como Ancelotti"
    #comment = "Felicitaciones al Real_Madrid, en las buenas y en las malas Visca Barza!"
    comment = "El mejor del F.C Barcelona en la final en mi opinion fue Pinto, el mejor del Real_Madrid aunque no marco fue Benzema, tiene mucha calidad."
    
    manager = EntitySA()
    manager.classify(comment, entidades_detectadas)
    
    
    
