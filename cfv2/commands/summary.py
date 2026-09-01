from cfv2.imports import *
from cfv2.core.fetch_gemini import *

@click.command()
@click.argument("name")
def summary(name):

    fetch_gemini(name)