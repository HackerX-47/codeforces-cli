from cfv2.functions import *
from cfv2.api import caller
from cfv2.display.submissions_display import *

def fetch_submissions_data(name, last, only_ac, lang, problem, opt = 0):

    count = last
    if opt == 0: count = 100000
    params = {"handle" : name, "from" : 1, "count" : count}
    data = caller("user.status", params)
    if data is None:
        return 

    df = pd.DataFrame(data)

    if only_ac: 
        df = df[df["verdict"] == "OK"]

    if lang:    
        df = df[df["programmingLanguage"].apply(normalize_lang)== lang.lower()]

    if problem: 
        df = df[df["problem"].apply(lambda x: x["index"].upper() == problem.upper())]

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

    keys = ["AC", "WA", "TLE", "MLE", "CE", "RE"]
    verdict_count = {key: 0 for key in keys}

    lang_dict = {
        "cpp"    : 0, "python" : 0, "java"   : 0, "kotlin" : 0, 
        "js"     : 0, "c#"     : 0, "go"     : 0, "others" : 0
    }

    df["problem_id"]    = df["problem"].apply(lambda x: (x.get("contestId"), x.get("index")))
    df["attempts"]      = df.groupby("problem_id")["problem_id"].transform("size")
    df["problem_rating"]= df["problem"].apply(lambda x: x.get("rating"))
    accepted            = df[df["verdict"] == "OK"]
    unique_accepted     = accepted.drop_duplicates(subset=["problem_id"])
    unique_attempted    = df.drop_duplicates(subset=["problem_id"])

    unique_accepted_cnt = len(unique_accepted)
    unique_attempted_cnt= len(unique_attempted)

    solved_by_rating    = unique_accepted["problem_rating"].dropna().value_counts().to_dict()
    attempted_by_rating = unique_attempted["problem_rating"].dropna().value_counts().to_dict()

    avg_solved_rating   = unique_accepted["problem_rating"].dropna().mean()
    highest_sol_rating  = int(unique_accepted["problem_rating"].max())
    lowest_solved_rating= int(unique_accepted["problem_rating"].min())

    ac_rate_by_rating = (
        df.dropna(subset=["problem_rating"])
        .groupby("problem_rating")["verdict"]
        .apply(lambda x: (x == "OK").mean() * 100)
        .round(2)
        .to_dict()
    )

    avg_attempts_to_solve = round(unique_accepted["attempts"].mean(), 2)

    if opt == 1:    header()

    for index, curr in df.iterrows():

        problem = df.loc[index, "problem"]
        lang    = df.loc[index, "programmingLanguage"]
        idx     = problem["index"]
        rating  = problem.get("rating", "-")
        verdict = status[df.loc[index, "verdict"]]

        lang_dict[normalize_lang(lang)] += 1
        verdict_count[verdict]          += 1 

        data1 = {
            "index" : idx, 
            "rating" : rating,
            "verdict" : verdict,
            "lang"  : lang
        }

        if opt == 1:
            print1(data1)

    m_lang = max(lang_dict, key=lang_dict.get) if any(lang_dict.values()) else "N/A"

    data2 = {
        "verdict_count"  : verdict_count, 
        "count"          : len(df), 
        "lang"           : m_lang,
        "unique_attempt" : unique_attempted_cnt,
        "unique_ac"      : unique_accepted_cnt,
        "attempt_rating" : attempted_by_rating,
        "solved_rating"  : solved_by_rating,
        "avg_sol_rating" : int(avg_solved_rating),
        "hi_sol_rating"  : highest_sol_rating,
        "lo_sol_rating"  : lowest_solved_rating,
        "ac_rate_rating" : ac_rate_by_rating,
        "avg_attempts"   : avg_attempts_to_solve
    }

    if(opt == 1):
        print2(data2)
    return data2