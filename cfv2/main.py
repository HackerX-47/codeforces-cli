from cfv2.imports import *
from cfv2.commands.user import user
from cfv2.commands.rating import rating
from cfv2.commands.submissions import submissions

@click.group()
def cli():
    pass

cli.add_command(user)
cli.add_command(rating)
cli.add_command(submissions)

if __name__ == "__main__":
    cli()