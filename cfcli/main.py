from cfcli.imports import *
from cfcli.commands.user import user
from cfcli.commands.rating import rating
from cfcli.commands.submissions import submissions

@click.group()
def cli():
    pass

cli.add_command(user)
cli.add_command(rating)
cli.add_command(submissions)

if __name__ == "__main__":
    cli()