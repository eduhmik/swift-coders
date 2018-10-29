import click
import psycopg2
from app.database import DbSetup,db_url
from getpass import getpass


class Register(DbSetup):
    """Normal user models"""
    def __init__(self, username, email, password, role='admin'):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        
    def add_user(self):
        """Save item to the database"""
        query = """
                INSERT INTO users(username, email, role, password)
                VALUES(%s, %s, %s, %s) RETURNING id
                """
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute(query, (
            self.username,
            self.email,
            self.role,
            self.password
            ))
        conn.commit()
    
   
      
