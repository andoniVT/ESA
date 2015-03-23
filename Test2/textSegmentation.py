#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 18/3/2015

@author: ucsp
'''
from nltk import tokenize
import itertools
import re
from __builtin__ import True

class Segmentation(object):
    
    def __init__(self , sentence):
        self.abbreviations = {'dr.': 'doctor', 'sr.': 'senior',  'sra.': 'seniora', 'srta.': 'seniorita', 'vs.': 'versus'}
        self.terminators = ['.', '!', '?' , ',' , ';' ,'pero' , 'sin embargo' , 'no obstante', 'por el contrario' ,
                               'en cambio' , 'con todo' , 'de todas maneras' , 'aunque', 'tampoco' ,
                                'porque' , 'por esta razon', 'por consiguiente' ,'asi pues' , 'de ahi que', 
                                'asi que', 'de modo que', 'es decir' , 'yy' , 'o sea', 'esto es', 'mejor dicho', 
                                'por ejemplo' , 'oo' ]
        self.wrappers = ['"', "'", ')', ']', '}']
        self.sentence = sentence
    
    def find_all(self, a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1:
                return
            yield start
            start += len(sub)
    
    def find_sentence_end(self ,paragraph):
        [possible_endings, contraction_locations] = [[], []]
        contractions = self.abbreviations.keys()
        sentence_terminators = self.terminators + [terminator + wrapper for wrapper in self.wrappers for terminator in self.terminators]
        for sentence_terminator in sentence_terminators:
            t_indices = list(self.find_all(paragraph, sentence_terminator))
            possible_endings.extend(([] if not len(t_indices) else [[i, len(sentence_terminator)] for i in t_indices]))
        for contraction in contractions:
            c_indices = list(self.find_all(paragraph, contraction))
            contraction_locations.extend(([] if not len(c_indices) else [i + len(contraction) for i in c_indices]))
        possible_endings = [pe for pe in possible_endings if pe[0] + pe[1] not in contraction_locations]
        if len(paragraph) in [pe[0] + pe[1] for pe in possible_endings]:
            max_end_start = max([pe[0] for pe in possible_endings])
            possible_endings = [pe for pe in possible_endings if pe[0] != max_end_start]
        possible_endings = [pe[0] + pe[1] for pe in possible_endings if sum(pe) > len(paragraph) or (sum(pe) < len(paragraph) and paragraph[sum(pe)] == ' ')]
        end = (-1 if not len(possible_endings) else max(possible_endings))
        return end 
    
    def find_sentences(self):
        especial_terminators = ["o" , "y" , "u"]
        list_sentence = self.sentence.split()
        sentence = ""
        for i in list_sentence:
            if i in especial_terminators:
                i = i+i
            sentence = sentence + i + " "
        self.sentence = sentence  
                
        end = True
        sentences = []
        while end > -1:
            end = self.find_sentence_end(self.sentence)
            if end > -1:
                sentences.append(self.sentence[end:].strip())
                self.sentence = self.sentence[:end]
        sentences.append(self.sentence)
        sentences.reverse()
        return sentences     
        
if __name__ == '__main__':
    
    #seg = Segmentation("Felicitaciones al Real Madrid, en las buenas y en las malas Visca Barza!")
    
    text = "El mejor del F.C Barcelona en la final en mi opinión fue Pinto, el mejor del Real Madrid aunque no marcó fue Benzema, tiene mucha calidad."
    seg = Segmentation(text)
    
    segmentos = seg.find_sentences()
    for i in segmentos:
        print i 
    
