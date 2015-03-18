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


if __name__ == '__main__':
    
    manager = EManager()
    manager.add_entity("movistar")
    
    entidades = manager.load_entities()
    print entidades
    
    