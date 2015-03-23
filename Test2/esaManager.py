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
            for j in entidades_detectadas:
                words = texto_sin_signos.split()
                for k in words:
                    if k==j:
                        texto = proc.get_processed_comment()
                        negation = proc.has_negation()
                        polaridad = em.find_polarity(texto, negation)
                        em.add_atributte(j, i, polaridad)
                        print texto
                        print negation
                        print polaridad
                        print em.polarity_rule(polaridad)
                            

if __name__ == '__main__':
    
    entidades_detectadas = ["movistar" , "claro"]
    comment = "movistar no es una pesima empresa , claro no es mucho mejor"
    
    manager = EntitySA()
    manager.classify(comment, entidades_detectadas)
    
    
    
