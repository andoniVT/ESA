import elementtree.ElementTree as ET
from elementtree.ElementTree import ElementTree


xml = "stompol-tweets-train-tagged.xml"

if __name__ == '__main__':
	
	arch = open(xml , 'r')
		
	for lines in arch:
		lines = lines.rstrip()
		aux = lines.find(">")+1
		texto = lines[aux:]
		  
		
		aux = texto.find("entity=")+8
		entity =  texto[aux:]
		
		
		texto2 = entity
		aux = entity.find("polarity")-2
		entity = entity[:aux]
		
		aux = texto.find("<")
		texto = texto[:aux]
		#print texto
		
		#print entity
		aux = texto2.find("=")+2
		polarity = texto2[aux:]
		texto2 = polarity
		#print texto2
		aux = polarity.find(">")-1
		polarity = polarity[:aux]
		
		aux = texto2.find(">")+1
		texto2 = texto2[aux:]
		
		
		texto3 = texto2
		aux = texto2.find("<")
		texto2 = texto2[:aux]
		
		texto = texto +texto2
		
		aux = texto3.find(">")+1
		texto3 = texto3[aux:]
		
		aux = texto3.find("<")
		texto3 = texto3[:aux]
		texto = texto + texto3
		print texto
		print " "   
	
	
	'''
	tree = ET.parse(xml)
	root = tree.getroot()
	iter = root.getiterator('tweet')
	for element in iter:
		print element.attrib
		for child in element:
			print child.text
		#print element.attrib
	'''
