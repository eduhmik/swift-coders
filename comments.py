from datetime import datetime
import psycopg2 
from psycopg2.extras import RealDictCursor
from database import db_url

'''class model for our comments'''
class Comment:

    def __init__(self, message, created_by=None):
        self.message = message
        self.created_by = created_by

    def insert(self):
        '''user inputs message'''
        # message = input('Enter a comment message')

        '''insert comment into database'''
        query = """
                INSERT INTO comments(message, created_by)
                VALUES(%s, %s) Returning id
                """
        conn = psycopg2.connect(db_url)
        cur =conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query,(
            self.message,
            self.created_by
        ))
        print('Comment added successfully')
        conn.commit()

        '''method for a user to edit message'''
        
    def edit_message(self, comments_id, message):
        '''user input to edit a message'''
        message = input("Enter a message to edit")
        conn =psycopg2.connect(db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("UPDATE comments SET message=%s WHERE comments_id = %s",(
            message,
            comments_id
        ))
        conn.commit()


        '''method to delete a comment message'''
        
    def delete_message(self, comments_id):
        conn = psycopg2.connect(db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("DELETE FROM comments WHERE comments_id=%s",(
            comments_id
        ))
        conn.commit()