from cfv2.imports import *

def header():

    print("\nuser details")
    print("----------------------------")
    return

def display(user_data):

    print("handle       : ", user_data["handle"])
    print("full name    : ", user_data["fullName"])
    print("max rating   : ", user_data["maxRating"])
    print("rank         : ", user_data["rank"]) 
    print("organization : ", user_data["org"])
    return