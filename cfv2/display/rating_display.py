from cfv2.imports import *

def header():

    print(
        f"\n{"CONTEST TYPE":<25}" 
        f"{"RANK":>10}" 
        f"{"ΔRATING":>10}" 
        f"{"CURR RATING":>12}"
    )

    print("─"*57)

def print1(df):

    for index, row in df.iterrows():
        print(
            f"{row['contestType']:<25}"
            f"{row['rank']:>10}"
            f"{row['ratingChange']:>+10}"
            f"{row['currRating']:>12}"
        )
        
def print2(data):

    print()
    print("RATING")
    print("────────────────────────────────────────")

    print("RATING OVERVIEW")
    print(f"  Current rating           : {data['currRating']}")
    print(f"  Best rating              : {data['bestRating']}")
    print(f"  Worst rating             : {data['worstRating']}")
    print(f"  Overall change           : {data['ovlRatingChng']:+}")

    print()
    print("CONTEST PERFORMANCE")
    print(f"  Total contests           : {data['totalContest']}")
    print(f"  Avg rating change        : {data['avgRatingChng']:+.2f}")
    print(f"  Positive contests        : {data['posChngCount']}")
    print(f"  Negative contests        : {data['negChngCount']}")
    print(f"  No change                : {data['noChngCount']}")

    print()
    print("RANK PERFORMANCE")
    print(f"  Best rank                : {data['bestRank']}")
    print(f"  Worst rank               : {data['worstRank']}")
    print(f"  Avg rank                 : {data['avgRank']}")

    return