'''
Created on 20/3/2015

@author: ucsp
'''

# tablas: entidad - comentario

import MySQLdb

class Connection(object):
    
    def __init__(self):
        self.__server = "localhost"
        self.__user = "root"
        self.__pass = "jorgeandoni"
        #self.__pass = "bayern"
        #self.__db = "test"
        self.__db = "esa"
        self.__conn = MySQLdb.connect(self.__server, self.__user, self.__pass, self.__db)
    
    def test(self):
        c = self.__conn.cursor()
        c.execute("SELECT * FROM persona")
        rows = c.fetchall()
        for i in rows:
            print i
    
    def add_entity(self, nombre_entidad):
        c = self.__conn.cursor()
        consulta =  'SELECT * FROM entidad WHERE nombre="%s"' % (nombre_entidad,) + ";"        
        c.execute(consulta)
        rows = c.fetchall()
        if len(rows) == 0:
            consulta2 = 'INSERT INTO entidad VALUES (NULL, "%s")' % (nombre_entidad,) + ";"
            c.execute(consulta2)
            print consulta2
        else:
            print "Entidad ya existe!"
    
    def add_attribute(self, nombre_entidad, atributo):
        c = self.__conn.cursor()
        consulta = 'SELECT id_entidad FROM entidad WHERE nombre="%s"' %(nombre_entidad,) + ";"
        c.execute(consulta)
        rows = c.fetchall()
        if len(rows)!=0:            
            id_entidad = rows[0][0]
            consulta2 = 'INSERT INTO comentario2 VALUES (NULL, "%s"' % (atributo[0],) + ", " + str(atributo[1]) + ", " + str(id_entidad) + ");"
            c.execute(consulta2)
            print consulta2
            
        else:
            print "Entidad no existe"
                  


if __name__ == '__main__':
    
    con = Connection()
    con.add_entity("claro")                   
    
    atributo = ["claro es una pesima empresa" , -1]
    
    con.add_attribute("claro", atributo)
    
    
        
        

