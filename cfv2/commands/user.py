from cfv2.core.fetch_user import *

@click.command()
@click.argument("name")
def user(name):

    fetch_user_data(name, opt = 1)
   