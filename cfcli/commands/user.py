from cfcli.imports import *
from cfcli.api import caller
from cfcli.gemini import ask_gemini

@click.command()
@click.argument("name")
def user(name):

    question = "What is today's date?"
    answer = ask_gemini(question)
    
    print("\nGemini: ")
    print(answer)

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

    print("🔥🔥🔥 NEW USER.PY IS RUNNING 🔥🔥🔥")
    print("\nxuser details")
    print("----------------------------")
    print("handle       : ", handle)
    print("full name    : ", fullName)
    print("max rating   : ", maxRating)
    print("rank         : ", rank) 
    print("organization : ", org)


    