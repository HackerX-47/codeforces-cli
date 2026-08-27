from cfv2.imports import *

def header():
    print(f"\n{"contest type":<25} {"rank":>10} {"Δrating":>10} {"new Rating":>10}")
    print("----------------------------------------------------------")

def print1(data):
    print(f"{data["contestType"]:<25} {data["rank"]:>10} {data["ratingChange"]:>+10} {data["currRating"]:>10}")

def print2(data):
    print("Total Contests: ", data["totalContest"])
    print("Current Rating: ", data["currRating"])