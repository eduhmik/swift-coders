import psycopg2
import click
from psycopg2.extras import RealDictCursor

db_url= "dbname = 'group_cli' user = 'postgres' host ='localhost' port ='5432' password='chacha'"
    
class DbSetup():
    def __init__(self):
        self.conn=psycopg2.connect(db_url)
   
    def create_tables(self):
        conn = self.conn
        curr = self.cursor()
        queries = self.tables()
        for query in queries:
            curr.execute(query)
        conn.commit()
    
    def tables(self):
        query1="""
        CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            username VARCHAR,
            email VARCHAR,
            role VARCHAR,
            password VARCHAR,
            created_on timestamp
        )
        """
        query2="""
        CREATE TABLE IF NOT EXISTS comments(
            id serial PRIMARY KEY,
            message VARCHAR,
            created_by VARCHAR,
            created_at timestamp
        )
        """
        queries=[query1,query2]
        return queries

    def cursor(self):
        cur=self.conn.cursor(cursor_factory=RealDictCursor)
        return cur
    

   


       
        