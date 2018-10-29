import click, sys
from models.comments import Comment


@click.command()
def login():

    username = input("Enter Username")
    password = input("Enter Your password")

    query = "SELECT * FROM users WHERE username = %s"
    cur.execute(query, (username))
    user = cur.fetchone()
    if not user:
        return "user not found"
    if user['password'] == password:
        print("Log in successful")
        message = input("Enter Your Comment")
        comment = comment(message, username)
        comment.insert()
    click.echo("invalid password")
    sys.exit()

@click.group()
def cli():
    pass

cli.add_command(login)


if __name__ == "__main__":
    cli()
