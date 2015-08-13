#import elementtree.ElementTree as ET
#from elementtree.ElementTree import ElementTree


xml = "stompol-tweets-train-tagged.xml"
xml2 = "socialtv-tweets-train-tagged.xml"

def prueba():
	arch = open(xml2 , 'r')
	comentarios = []
	for lines in arch:
		comentario = []
		lines = lines.rstrip()
		aux = lines.find(">")+1
		lines = lines[aux:]
		aux = lines.find("</tweet>")
		lines = lines[:aux]
		aux = lines.find("<sentiment")
		while aux != -1:
			texto = lines[:aux]
			lines = lines[aux:]
			aux = lines.find("entity=")+8
			entity = lines[aux:]		
			texto2 = entity
		 	aux = entity.find("polarity")-2
			entity = entity[:aux]
			aux = texto.find("<")
			texto = texto[:aux]
			aux = texto2.find("=")+2
			polarity = texto2[aux:]
			texto2 = polarity		
			aux = polarity.find(">")-1
			polarity = polarity[:aux]
			aux = texto2.find(">")+1
			texto2 = texto2[aux:]			
			aux = texto2.find("</sentiment>")
			texto3 = texto2
			texto2 = texto2[:aux]
			texto = texto + " " +texto2
			aux = texto3.find(">")+1
			texto3 = texto3[aux:] 			
			aux = texto3.find("<sentiment")
			if aux == -1:			
				texto = texto + texto3								
			lines = texto3
			contenido = [texto, entity, polarity]
			
			#print contenido
			comentario.append(contenido)
			
			#print " "
		comentarios.append(comentario)
		#print "---"
		
	for i in comentarios:
		print i 
		
 
		
	
	
	

if __name__ == '__main__':
	
	arch = open(xml , 'r')
	prueba()
		
	'''
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
	
	

	
