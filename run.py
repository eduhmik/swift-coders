import click
from getpass import getpass
from database import DbSetup
from register import Register


db=DbSetup()

@click.command()
def register ():
        """this registers a normal user"""
        username = input('Enter username: ')
        email = input('Enter email: ')
        password = getpass('Enter password: ')
        
        try:
            assert password == getpass('Confirm password: ')
        except AssertionError as e:
            print('The password did match, try again')
            
        user = Register(username, email, password)
        user.add_user()
        print('Admin created successfully')
@click.command()
def create_tables():
    db.create_tables()
@click.group()
def cli():
    pass
  

cli.add_command(register)
cli.add_command(create_tables)

if __name__ == "__main__":
    cli()



