from cfv2.imports import *
from cfv2.core.fetch_graph import *


@click.command()
@click.argument("name")
def graph(name):

    fetch_graph(name)