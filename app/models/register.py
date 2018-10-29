import click
import psycopg2

class Register():
    """Normal user models"""
    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        
    def add_user(self):
        """Save item to the database"""
        query = """
                INSERT INTO users(username, email, role, password)
                VALUES(%s, %s, %s, %s, %s) RETURNING id
                """
        conn = psycopg2.connect(self)
        cur = conn.cursor()
        cur.execute(query, (
            self.username,
            self.email,
            self.role,
            )
        conn.commit()

    def register (self):
        """this registers a normal user"""
        username = input('Enter username: ')
        email = input('Enter email: ')
        password = getpass('Enter password: ')
        role = ROLES['ADMIN']
        try:
            assert password == getpass('Confirm password: ')
        except AssertionError as e:
            print('The password did match, try again')
            return
        user = User(username, email, password, role)
        user.insert()
        print('Admin created successfully')
