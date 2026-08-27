from cfv2.imports import *
from cfv2.api import caller
from cfv2.gemini import ask_gemini

@click.command()
@click.argument("name")
def user(name):

    params = {"handles" : name}
    data = caller("user.info", params)
    if data is None:
        return 

    user = data[0]

    handle    = user.get("handle")
    first     = user.get("firstName") or ""
    last      = user.get("lastName") or ""
    fullName  = f"{first} {last}".strip() or "N/A"
    rating    = user.get("rating") or "Unrated"
    rank      = user.get("rank").capitalize() or "Unrated"
    maxRating = user.get("maxRating") or "Unrated"
    org       = user.get("organization") or "N/A"

    print("\nuser details")
    print("----------------------------")
    print("handle       : ", handle)
    print("full name    : ", fullName)
    print("max rating   : ", maxRating)
    print("rank         : ", rank) 
    print("organization : ", org)


    question = "25*3? in number only"
    answer = ask_gemini(question)
        
    print("\nGemini: ")
    print(answer)