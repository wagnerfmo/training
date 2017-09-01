import mysql.connector
import mysql_conf as cfg

class Dao():
    def __init__(self):
        self.cnx = mysql.connector.connect(user=cfg.mysql['user'], password=cfg.mysql['passwd'], host=cfg.mysql['host'], database=cfg.mysql['db'])
    
    def select(self, query_string):
        self.cur = self.cnx.cursor()
        self.cur.execute(query_string)
        resultset = self.cur.fetchone()
        return resultset
    
    def selectAll(self, query_string):
        self.cur = self.cnx.cursor()
        self.cur.execute(query_string)
        resultset = self.cur.fetchall()
        return resultset        
        
    def delete(self,  query_string):
        self.cur = self.cnx.cursor()
        try:
            self.cur.execute(query_string)
            self.cnx.commit()
        except:
            self.cur.rollback()
            
    def update(self, query_string):
        self.cur = self.cnx.cursor()
        try:
            self.cur.execute(query_string)
            self.cnx.commit()
        except:
            self.cur.rollback()
        
    def insert(self, query_string):
        self.cur = self.cnx.cursor()
        self.cnx.commit()
        try:
            self.cur.execute(query_string)
        except:
            self.cur.rollback()
                 
    def close_conx(self):
        self.cnx.close()
        
