import click
import sys
import psycopg2
from psycopg2.extras import RealDictCursor
from database import db_url
from comments import Comment




@click.command()
def login():

    username = input("Enter Username :")
    password = input("Enter Your password :")

    query = "SELECT * FROM users WHERE username = %s"
    conn=psycopg2.connect(db_url)
    cur=conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, (username,))
    user = cur.fetchone()
    if not user:
        return "user not found"
    if user['password'] == password:
        print("Log in successful")
        message = input("Enter Your Comment :")
        comment = Comment(message,username)
        comment.insert()
    else:
        click.echo("invalid password")
        sys.exit()

@click.group()
def cli():
    pass

cli.add_command(login)


if __name__ == '__main__':
    cli()
