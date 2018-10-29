from datetime import datetime
import psycopg2 
from psycopg2.extras import RealDictCursor

'''class model for our comments'''
class Comment():

    def __init__(self, message, created_at=datetime.now(), created_by=None):
        self.message = message
        self.created_at = created_at
        self.created_by = created_by

    def insert(self, message):
        '''user inputs message'''
        message = input('Enter a comment message')

        '''insert comment into database'''
        query = """
                INSERT INTO comments(message, created_at, created_by)
                VALUES(%s, %s, %s) Returning comments_id
                """
        conn = psycopg2.connect(self)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query,(
            self.message,
            self.created_at,
            self.created_by
        ))
        conn.commit()

        '''method for a user to edit message'''
        @classmethod
        def edit_message(cls, comments_id, message):
            '''user input to edit a message'''
            message = input("Enter a message to edit")
            conn = psycopg2.connect(self)
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("UPDATE comments SET message=%s WHERE comments_id = %s",(
                message,
                comments_id
            ))
            conn.commit()


        '''method to delete a comment message'''
        @classmethod
        def delete_message(cls, comments_id):
            conn = psycopg2.connect(self)
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("DELETE FROM comments WHERE comments_id=%s",(
                comments_id
            ))
            conn.commit()