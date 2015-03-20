'''
Created on 20/3/2015

@author: ucsp
'''

import MySQLdb

class Connection(object):
    
    def __init__(self):
        self.__server = "localhost"
        self.__user = "root"
        self.__pass = "jorgeandoni"
        self.__db = "test"
        self.__conn = MySQLdb.connect(self.__server, self.__user, self.__pass, self.__db)
    
    def test(self):
        c = self.__conn.cursor()
        c.execute("SELECT * FROM persona")
        rows = c.fetchall()
        for i in rows:
            print i 


if __name__ == '__main__':
    
    con = Connection()
    con.test()                    
    
    
        
        

