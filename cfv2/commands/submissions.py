from cfv2.core.fetch_submissions import *

@click.command()
@click.option("--last", default=20, show_default=True, type=int, help = "Show last n submissions")
@click.option("--only-ac", is_flag=True, default=False, help="Show only accepted submissions")
@click.option("--lang", default=None,
            type=click.Choice(["cpp", "python", "java", "kotlin", "js", "c#", "go", "others"], 
                    case_sensitive=False), help="Filter by language")
@click.option("--problem", default=None, help="Filter by problem index, e.g. A, B, C1")
@click.argument("name")
def submissions(name, last, only_ac, lang, problem):

    fetch_submissions_data(name, last, only_ac, lang, problem, opt = 1)
    