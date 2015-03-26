#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

''' path  '''
path_cicc = '/home/ucsp/workspace/SentimentManager'
path_home = '/home/andoni/Escritorio/PythonProjets/SentimentAnalizer'
path = path_cicc
#path = path_home

'''resource '''
big_text = path + '/resource/big2.txt'
stop_words = path + '/resource/stopwords_spanish.txt'

''' data test and training '''
trainSpanish = path + '/data/train/spanishTrain.xml'
trainPeruvian = path + '/data/train/peruvianTrain.xml'
testSpanish = path + '/data/test/spanishTest.xml'
testPeruvian = path + '/data/test/peruvianTest.xml'
prueba = path + '/data/train/prueba.xml'


''' suppervised classifiers '''
spanish_path = path + '/data_trained/classifiers_trained/spanish'
spanish_classifiers_two_classes_simple = spanish_path +  '/2_classes/simple'
spanish_classifiers_two_classes_tf_idf = spanish_path + '/2_classes/tf-idf'
spanish_classifiers_two_classes_lsa = spanish_path + '/2_classes/lsa'

spanish_classifiers_three_classes_simple = spanish_path + '/3_classes/simple'
spanish_classifiers_three_classes_tf_idf = spanish_path + '/3_classes/tf-idf'
spanish_classifiers_three_classes_lsa = spanish_path + '/3_classes/lsa'

svm = '/SupportVectorMachineCorpus.pk1'
naiveBayes = '/NaiveBayesCorpus.pk1'
maxEntropia = '/MaximaEntropiaCorpus.pk1'
decTree = '/DecisionTreeCorpus.pk1'

''' vector model '''
vspanish_path = path + '/data_trained/vector_model/spanish'
vector_models_two_classes =  vspanish_path + '/2_classes'
vector_model_three_classes = vspanish_path + '/3_classes'


''' unsupervised '''
# Recursos Lexicos 
#NEW_VOCABULARY = "path + '/resource/dictionary/groups/"
EMOTICONS = path + "/resource/emoticons.txt"
BOOSTER_WORDS_SPANISH = path + "/resource/booster_words_spanish.txt"
SENTIMENT_WORDS_SPANISH = path + "/resource/sentiment_words_spanish.txt"
SLANGS_PERUVIAN = path + "/resource/slangs_peruvian.txt"
NEGATING_WORDS_SPANISH = path + "/resource/negating_words_spanish.txt"
COMBINATIONS_SPANISH  = path + "/resource/combinations_spanish.txt"
COMBINATIONS_SLANGS_PERUVIAN = path + "/resource/combinations_slangs_peruvian.txt"
PUNCTUATION = path + "/resource/punctuation.txt"
STOPWORDS_SPANISH_OPINION_MINING = path + "/resource/stopwords_spanish_opinion_mining.txt"

# Tipos de Terminos
TERM_TYPE_EMOTICON = 'emoticon'
TERM_TYPE_BOOSTER = 'booster'
TERM_TYPE_WORD_SLANG = 'word_slang'
TERM_TYPE_COMBINATION = 'combination'
TERM_TYPE_NEGATING = 'negating'
TERM_TYPE_PUNCTUATION = 'punctuation'
TERM_TYPE_NEUTRO = 'neutro'

# Simbolos adicionales
FLEXIS_SIMBOL = '#'
SPLITTER_WEIGHTS = '=='
ENCODING = 'utf-8'
TERM_NOT_FOUND = ''
SPLITTER_FREQUENT_WORD = '<##>'




if __name__ == '__main__':
    
    print vector_models_two_classes
