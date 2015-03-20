'''
Created on 20/3/2015

@author: ucsp
'''

import MySQLdb

conn = MySQLdb.connect("localhost" , "root" , "jorgeandoni" , "test")
c = conn.cursor()
c.execute("SELECT * FROM persona")
rows = c.fetchall()

for i in rows:
    print i 


