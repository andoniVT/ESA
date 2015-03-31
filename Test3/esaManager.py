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
        #sentiment = obj.get_label()
        sentiment = obj.get_score()
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
            print i 
            proc = CP(i)
            texto_sin_signos = proc.remove_punctuation(i)            
            for j in entidades_detectadas:
                words = texto_sin_signos.split()
                for k in words:
                    if k==j:
                        polaridad = manager.classify(i)
                        em.add_atributte(j, i, polaridad)
                        print j + ": "  + str(polaridad)
    
    def analyze_entity(self, nombre_entidad):
        em = EM()
        per_values = em.get_values(nombre_entidad)
        if len(per_values)!=0:
            print "Entidad " + nombre_entidad + ": "
            print "menciones: " + str(per_values[0])
            print "positivos: " + str(round(per_values[1],2)) + "%"
            print "neutros: " + str(round(per_values[2],2)) + "%"
            print "negativos: " + str(round(per_values[3],2)) + "%"
         
                         
if __name__ == '__main__':
    #comment = "movistar es una pesima empresa , claro es mucho mejor"
    #comment = "El Barza en 7 dias ha quedado fuera de la lucha por los titulos. Hacen falta cambios tanto en la plantilla como en el estilo"
    #comment = "movistar es una pesima empresa sin embargo me gustan sus celulares"
    #comment = "Siendo un defensor del trabajo de Mourinho, no dejo de admirar la naturalidad en la victoria de un tecnico como Ancelotti"
    #comment = "Felicitaciones al Real_Madrid, en las buenas y en las malas Visca Barza!"
    comment = "El mejor del F.C Barcelona en la final en mi opinion fue Pinto, el mejor del Real_Madrid aunque no marco fue Benzema, tiene mucha calidad."
    text2 = "Tranquilos, messi se esta dosificando para el mundial... Que tiemble brasil!!"
    text3 = "Mi casa, mi familia, mi novia y mi Madrid ganando la copa al Barza...no se puede pedir nada más. #HalaMadrid"
    text4 = "Donde están los que decían que Gareth_Bale no valía cien millones? Jaja Habladores! HALA MADRID"
    text6 = "Si no os digo cada vez que habla Ramos lo mucho que me encanta su voz y su acento tampoco me quedo tranquila"
    text7 = "Alves echate unos bailes con Neymar para celebrar la copa del rey , del MADRID !! #HalaMadrid !"
    text8 = "Una lectura positiva de todo esto, los señores Messi y Neymar ya podéis pensar en el mundial de los cojones. Id tranquilos chicos"
    text9 = "Sergio_Ramos subiendo a recoger la copa con la bandera del Betis pa tocar los cojones"
    text10 = "Real como no quererte si siempre demuestras quien eres en la cancha"
    text11 = "Tanto Messi y Neymar y al final el Madrid sin Cristiano gana la copa"
    text12 = "Su salvador supremo Messi no pateo ni una lata en ese partido, la burla"
    text13 = "Si le dan la copa a Cristiano lloro de seguro"
    text14 = "Y por último, grandísima noticia la vuelta del Bale de la Premier, a los espacios y sin Cristiano, él gana partidos. Mucho mejor que Neymar"
    text15 = "Me da rabia que el Real_Madrid haya ganado, pero es lo qie hay"
    text16 = "Como juega mi Madrid como se quedan los catalanes HALA MADRID"
    text18 = "espectacular el Madrid y Gareth_Bale.  2-1 y para casa los del Barza jajaja"
    text19 = "Cuantaaaa felicidad despues de una tarde perfecta , el Madrid ganaaa la copa del rey al Barza!"
    text20 = "El Barza tiene que hacer muchos cambios, empezando por la directiva"
    text21 = "Cuidado que a Ramos no se le caiga esta vez la Copa_del_Rey :)"
    text22 = "Que supremacia la de Bale se los dije, EL PRÍNCIPE GALES Bale  haciendo añicos al Barza."
    text23 ="Los q hoy están Jodidos con el Barza, recuerden q estos saldrán hoy de fiesta y les importa una mierda empezando por Alves y por Neymar"
    text24 = "Me voy a cenar. Enhorabuena a los aficionados merengues. Lo del Barza es para hacérselo mirar,en una semana temporada en blanco. PATÉTICO!"
    text25 = "buen partido de los mandriles. ahora si, me da pena que el reportero de tve no busque la entrevista con Bale #nohablamosingles"
    text26 = "Los del Barcelona estan alterados no se , puras excusas"
    text27 = "Lo mataría al relator, a los del Real y mas a Cristiano! Ah, y a los ""simpatizantes"" del Real"
    text28 = "El Tata_Martino se gana solito la destitucion, Alexis y Pedro estan muchisimo mejores que Neymar, pero la plata es la que juega"
    text29 = "Triunfo merecido, messi desaparecido, Pinto fatal un equipo de primer nivel se merece un portero al menos de garantias y que tenga reflejos"
    text30 = "El Barcelona gana un titulo y es una temporada mediocre, el Madrid gana una copa y es un temporadon!!"
    
    entidades_detectadas = [ "Barcelona" , "Madrid" ]    
    manager = EntitySA()    
    
    manager.classify(text30, entidades_detectadas)
    
    manager.analyze_entity("Barcelona")
    manager.analyze_entity("Madrid")
    
    
    
