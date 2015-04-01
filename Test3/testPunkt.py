'''
Created on 31/3/2015

@author: ucsp
'''

import nltk.tokenize.punkt
import pickle
import codecs

filename = "testTrain.txt"
filename2 = "testTrain.pk"

tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
text = codecs.open(filename, "r", "utf8").read()
tokenizer.train(text)
out = open(filename2 , "wb")
pickle.dump(tokenizer, out)
out.close()

file = open(filename2, 'r')
segmenter = pickle.Unpickler(file).load()

text = "El Barcelona gana un titulo y es una temporada mediocre. el Madrid gana una copa . es un temporadon"
sentences = segmenter.tokenize(text)

for i in sentences:
    print i               





if __name__ == '__main__':
    
    print "hello!" 