from cfv2.functions import *
from cfv2.api import caller
from cfv2.display.rating_display import *

def fetch_rating_data(name, opt = 0):

    params  = {"handle" : name}
    data    = caller("user.rating", params)
    if data is None:
        return 

    df = pd.DataFrame(data)

    df["ratingChange"]  = df["newRating"] - df["oldRating"]
    df["datetime"]      = pd.to_datetime(df["ratingUpdateTimeSeconds"], unit="s", utc = True).dt.tz_convert("Asia/Kolkata")
    df["month"]         = df["datetime"].dt.to_period("M")

    totalContests   = len(df)
    best_rank       = 0
    worst_rank      = float('inf')
    avg_rank        = 0
    avg_rating_chng = 0
    pos_chng_count  = 0
    neg_chng_count  = 0
    no_chng_count   = 0
    best_rating     = 0
    worst_rating    = float('inf')
    ovl_rating_chng = df["ratingChange"].sum()
    
    
    m_grp = df.groupby("month").agg(
        rating_start=("oldRating", "first"),
        rating_end=("newRating", "last"),
        rating_change=("ratingChange", "sum")
    )

    if opt == 1:    header();

    for index, curr in df.iterrows():

        contestName  = df.loc[index, "contestName"]
        matches      = re.findall(r"Div\. ?\d", contestName)
        currRating   = df.loc[index, "newRating"]
        ratingChange = df.loc[index, "newRating"]-df.loc[index, "oldRating"]
        rank         = df.loc[index, "rank"]

        best_rank        = max(rank, best_rank)
        worst_rank       = min(rank, worst_rank)
        avg_rank        += rank/totalContests
        avg_rating_chng += ratingChange/totalContests
        best_rating      = max(currRating, best_rating)
        worst_rating     = min(currRating, worst_rating)

        if ratingChange > 0:    pos_chng_count += 1
        if ratingChange < 0:    neg_chng_count += 1


        if matches: contestType = " + ".join(matches)
        else:       contestType = contestName

        data1 = {
            "contestType" : contestType,
            "rank" : rank, 
            "ratingChange" : ratingChange,
            "currRating" : currRating
        }

        if opt == 1: print1(data1)

    no_chng_count = totalContests - (pos_chng_count + neg_chng_count)

    data2 = {
        "totalContest"      : totalContests, 
        "currRating"        : df.iloc[-1]["newRating"],
        "bestRank"          : best_rank,
        "worstRank"         : worst_rank,
        "avgRank"           : avg_rank,
        "avgRatingChng"     : avg_rating_chng,
        "posChngCount"      : pos_chng_count,
        "negChngCount"      : neg_chng_count,
        "noChngCount"       : no_chng_count,
        "bestRating"        : best_rating,
        "worstRating"       : worst_rating,
        "ovlRatingChng"     : ovl_rating_chng,
        "m_rating_analysis" : m_grp
    }

    if opt == 1:
        print()
        print2(data2)

    return data2