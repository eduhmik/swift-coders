import click

@click.command()
def login(username, password):

    username = input("Enter Username")
    password = input("Enter Your password")

    query = "SELECT * FROM users WHERE username = %s"
    cur.execute(query, (username))
    user = cur.fetchone()
    if not user:
        return "user not found"
    if user['password'] == password:
        pass
    return "invalid password"

@click.group()
def cli():
    pass

cli.add_command(login)

