from cfv2.functions import *
from cfv2.api import caller
from cfv2.display.rating_display import *

def fetch_rating_data(name, opt = 0):

    params = {"handle" : name}
    data = caller("user.rating", params)
    if data is None:
        return 

    header();

    for curr in data:

        contestName = curr["contestName"]
        matches = re.findall(r"Div\. ?\d", contestName)
        ratingChange = curr["newRating"]-curr["oldRating"]
        rank = curr["rank"]

        if matches: contestType = " + ".join(matches)
        else:       contestType = contestName

        data1 = {
            "contestType" : contestType,
            "rank" : rank, 
            "ratingChange" : ratingChange,
            "currRating" : curr["newRating"]
        }

        if opt == 1: print1(data1)

    data2 = {
        "totalContest"  : len(data), 
        "currRating"    : data[-1]["newRating"]
    }

    if opt == 1:
        print()
        print2(data2)

    return data2