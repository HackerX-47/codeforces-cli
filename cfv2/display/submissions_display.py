from cfv2.imports import *

def header():
    print(f"\n{"prob":<5} {"rating":<10} {"verdict":<10} {"lang":<20}")
    print("----------------------------------------------------")

def print1(data):
    print(f"{data["index"]:<5} {data["rating"]:<10} {data["verdict"]:<10} {data["lang"]:<20}")

def print2(st_dict):

    ac_count = st_dict["ac"]
    count = st_dict["count"]
    accuracy = (ac_count/count)*100 if count else 0
    print()
    print("Summary")
    print("------------------")
    print("AC           : ", ac_count)
    print("Total        : ", count)
    print("Accuracy     : ", f"{accuracy:.2f}%")
    print("Top Language : ", st_dict["lang"])
    return