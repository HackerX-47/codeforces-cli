from cfv2.core.fetch_rating import *

@click.command()
@click.argument("name")
def rating(name):

    fetch_rating_data(name, opt = 1)