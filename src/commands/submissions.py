from functions import *
from api import caller

@click.command()
@click.option("--last", default=20, show_default=True, type=int, help = "Show last n submissions")
@click.option("--only-ac", is_flag=True, default=False, help="Show only accepted submissions")
@click.option("--lang", default=None,
            type=click.Choice(["cpp", "python", "java", "kotlin", "js", "c#", "go", "others"], 
                    case_sensitive=False), help="Filter by language")
@click.option("--problem", default=None, help="Filter by problem index, e.g. A, B, C1")
@click.argument("name")
def submissions(name, last, only_ac, lang, problem):

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

    print(f"\n{"prob":<5} {"rating":<10} {"verdict":<10} {"lang":<20}")
    print("----------------------------------------------------")

    for curr in data:
        
        problem = curr["problem"]

        idx = problem["index"]
        rating = problem.get("rating", "-")
        lang = curr["programmingLanguage"]
        verdict = status[curr["verdict"]]

        lang_dict[normalize_lang(lang)] += 1
        if verdict == "AC": ac_count += 1

        print(f"{idx:<5} {rating:<10} {verdict:<10} {lang:<20}")

    m_lang = max(lang_dict, key=lang_dict.get) if any(lang_dict.values()) else "N/A"
    st = {"ac" : ac_count, "count" : len(data), "lang" : m_lang}
    summary(st)