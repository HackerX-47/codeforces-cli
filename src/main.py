from imports import *
from commands.user import user
from commands.rating import rating
from commands.submissions import submissions

@click.group()
def cli():
    pass

cli.add_command(user)
cli.add_command(rating)
cli.add_command(submissions)

if __name__ == "__main__":
    cli()