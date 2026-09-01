from cfv2.imports import *
from cfv2.api import caller
from cfv2.display.user_display import *

def fetch_user_data(name, opt = 0):

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

    user_data = {
        "handle"    : handle,
        "fullName"  : fullName,
        "maxRating" : maxRating,
        "rank"      : rank,
        "org"       : org
    }

    if opt == 1:
        header()
        display(user_data)  
       
    return data