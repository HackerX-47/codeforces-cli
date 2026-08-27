from cfv2.functions import *
from cfv2.api import caller
from cfv2.display.submissions_display import *

def fetch_submissions_data(name, last, only_ac, lang, problem, opt = 0):

    count = last
    params = {"handle" : name, "from" : 1, "count" : count}
    data = caller("user.status", params)
    if data is None:
        return 

    if only_ac: 
        data = [d for d in data if d["verdict"] == "OK"]

    if lang:    
        data = [d for d in data if normalize_lang(d["programmingLanguage"]) == lang.lower()]

    if problem: 
        data = [d for d in data if d["problem"]["index"].upper() == problem.upper()]

    if not data:
        print()
        print("No submissions match the given filters.")
        return

    status = {
        "OK"                    : "AC",
        "WRONG_ANSWER"          : "WA",
        "TIME_LIMIT_EXCEEDED"   : "TLE",
        "MEMORY_LIMIT_EXCEEDED" : "MLE",
        "RUNTIME_ERROR"         : "RE",
        "COMPILATION_ERROR"     : "CE",
    }

    lang_dict = {
        "cpp"    : 0, "python" : 0, "java"   : 0, "kotlin" : 0, 
        "js"     : 0, "c#"     : 0, "go"     : 0, "others" : 0
    }

    ac_count = 0

    if opt == 1:    header()

    for curr in data:
        
        problem = curr["problem"]

        idx = problem["index"]
        rating = problem.get("rating", "-")
        lang = curr["programmingLanguage"]
        verdict = status[curr["verdict"]]

        lang_dict[normalize_lang(lang)] += 1
        if verdict == "AC": ac_count += 1

        data1 = {
            "index" : idx, 
            "rating" : rating,
            "verdict" : verdict,
            "lang"  : lang
        }

        if opt == 1:
            print1(data1)

    m_lang = max(lang_dict, key=lang_dict.get) if any(lang_dict.values()) else "N/A"
    st = {"ac" : ac_count, "count" : len(data), "lang" : m_lang}

    if(opt == 1):
        print2(st)

    return st