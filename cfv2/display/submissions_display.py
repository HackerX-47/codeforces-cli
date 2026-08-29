from cfv2.imports import *

def header():

    print(
        f"\n{"TYPE":<5}"
        f"{"RATING":<10}"
        f"{"VERDICT":<10}"
        f"{"LANG":<20}"
    )
    
    print("─"*49)

def print1(df):

    for index, row in df.iterrows():
        print(
            f"{row['index']:<5}"
            f"{row['rating']:<10}"
            f"{row['verdict']:<10}"
            f"{row['lang']:<20}"
        )

def print2(st_dict):

    ac_count = st_dict["verdict_count"]["AC"]
    count = st_dict["count"]
    accuracy = (ac_count/count)*100 if count else 0

    print()
    print("SUMMARY")
    print("────────────────────────────────────────")

    print("SUBMISSIONS")
    print(f"  Total submissions       : {st_dict['count']}")
    print(f"  Accepted                : {st_dict['verdict_count']['AC']}")
    print(f"  Accuracy                : {accuracy:.2f}%")
    print(f"  Top language            : {st_dict['lang']}")

    print()
    print("PROBLEM PROGRESS")
    print(f"  Unique attempted        : {st_dict['unique_attempt']}")
    print(f"  Unique solved           : {st_dict['unique_ac']}")
    print(f"  Avg attempts / solve    : {st_dict['avg_attempts']:.2f}")

    print()
    print("PROBLEM DIFFICULTY")
    print(f"  Avg solved rating       : {st_dict['avg_sol_rating']}")
    print(f"  Highest solved rating   : {st_dict['hi_sol_rating']}")
    print(f"  Lowest solved rating    : {st_dict['lo_sol_rating']}")

    return