#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18/3/2015

@author: ucsp
'''

import json
import cPickle
import os.path
import re 

fileEntidades = "entidades.pk1"
vocabulary = 'resource/slangs_peruvian.txt'
vocabulary2 = 'resource/sentiment_words_spanish.txt'

class EManager():
    
    def __init__(self):
        if os.path.exists(fileEntidades):
            self.__entities = self.load_entities()
        else:
            self.__entities = []
    
    def load_entities(self):
        with open(fileEntidades , 'rb') as fid:
            load = cPickle.load(fid)
        return load 
    
    def save_file(self, file):
        with open(fileEntidades , 'wb') as fid:
            cPickle.dump(file, fid)
    
    def exits_entity(self, entidades, entidad):
        for i in entidades:
            if i[0] == entidad:
                return True
        return False
    
    def add_entity(self, nombre_entidad):
        entidad = [nombre_entidad, []]
        if not self.exits_entity(self.__entities, nombre_entidad):
            self.__entities.append(entidad)
        else:
            print "Entidad ya existe"  
        self.save_file(self.__entities)
    
    def add_attribute(self, nombre_entidad, atributo):
        for i in self.__entities:
            if i[0] == nombre_entidad:
                i[1].append(atributo)
        self.save_file(self.__entities)
    
    def load_value(self, word):
        lista = dict()
        file = open(vocabulary, 'r')
        file2 = open(vocabulary2, 'r')  
        files = [file, file2]
        for i in files:
            while True:
                line = i.readline()
                if not line: break;
                tmp = re.split("=", line)
                lista[tmp[0]] = tmp[2].rstrip()
        if lista.has_key(word):
            return int(lista[word])
        else:
            return 0
    
    def update_polarity(self, nombre_entidad, value):
        for i in self.__entities:
            if i[0] == nombre_entidad:
                for j in i[1]:
                    if j[2] == "NULL":
                        j[2] = value
        self.save_file(self.__entities)
    
    def find_polarity(self, lista_entidades):
        suma = 0.0
        n = 0
        for i in self.__entities:
            for e in lista_entidades:
                if i[0] == e:
                    posicion = len(i[1])-1
                    sentence = i[1][posicion][1]
                    list_sentence = sentence.split()
                    for j in list_sentence:
                        suma+=self.load_value(j)
                        n+=1
                    value = suma/n
                    print i[0]
                    print value
                    self.update_polarity(i[0], value)
                    suma=0.0
                    n=0
                    print ""
    
    def polarity_rule(self, value):
        if value>0: return "positivo"
        if value<0: return "negativo"
        if value==0: return "neutral"
         
    
    def get_entity_polarity(self, lista_entidades):
        for i in lista_entidades:
            for j in self.__entities:
                if i == j[0]:        
                    position = len(j[1])-1
                    polarity = self.polarity_rule(j[1][position][2])  
                    print i + " : "  + polarity  
                                            
    def print_entities(self):
        for i in self.__entities:
            for j in i:
                print j 
    

if __name__ == '__main__':
    
    manager = EManager()
    
    manager.get_entity_polarity(["movistar" , "empresa", "celulares"])
    
    #manager.add_entity("movistar")
    #atributo = ["el presidente arruino todo" , "president arruin todo" , 0]
    #manager.add_attribute("movistar", atributo)
    
    #manager.add_entity("empresa")
    #manager.add_attribute("empresa" , atributo)
    
    #manager.find_polarity(["movistar" , "empresa, claro"])
    #manager.print_entities()
    
    
    
    