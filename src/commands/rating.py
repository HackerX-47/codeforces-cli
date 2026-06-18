from functions import *
from api import caller

@click.command()
@click.argument("name")
def rating(name):

    params = {"handle" : name}
    data = caller("user.rating", params)
    if data is None:
        return 

    print(f"\n{"contest type":<25} {"rank":>10} {"Δrating":>10} {"new Rating":>10}")
    print("----------------------------------------------------------")

    for curr in data:

        contestName = curr["contestName"]
        matches = re.findall(r"Div\. ?\d", contestName)
        ratingChange = curr["newRating"]-curr["oldRating"]
        rank = curr["rank"]

        if matches: contestType = " + ".join(matches)
        else:       contestType = contestName

        print(f"{contestType:<25} {rank:>10} {ratingChange:>+10} {curr["newRating"]:>10}")

    print()
    print("Total Contests: ", len(data))
    print("Current Rating: ", data[-1]["newRating"])