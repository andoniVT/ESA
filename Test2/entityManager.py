'''

@author: andoni
Created on 22/03/2015
'''
from Test2.dbConnection import Connection
import re 

vocabulary = 'resource/slangs_peruvian.txt'
vocabulary2 = 'resource/sentiment_words_spanish.txt'

class EManager(object):
    
    def __init__(self):
        self.__con = Connection()
    
    def add_entities(self, entidades):
        for i in entidades:
            self.__con.add_entity(i)
    
    def add_atributte(self, entidad, texto, polaridad):
        atributo = [texto, polaridad]
        self.__con.add_attribute(entidad, atributo) 
        
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
        
    def find_polarity(self, texto, negation):
        suma = 0.0
        n = 0
        lista = texto.split()
        for i in lista:
            suma+=self.load_value(i)
            n+=1
        value = suma/n 
        if negation:
            value = -value
        return value 
    
    def polarity_rule(self, value):
        if value>0: return "positivo"
        if value<0: return "negativo"
        if value==0: return "neutral"
    
        



if __name__ == '__main__':
    
    e = EManager()
    print e.load_value("misio") 