from cfv2.functions import *
from cfv2.api import caller
from cfv2.display.submissions_display import *

def fetch_submissions_data(name, last, only_ac, lang, problem, opt = 0):

    count   = last
    if opt == 0: count = 100000
    params  = {"handle" : name, "from" : 1, "count" : count}
    data    = caller("user.status", params)

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
    df["datetime"]      = pd.to_datetime(df["creationTimeSeconds"], unit="s", utc = True).dt.tz_convert("Asia/Kolkata")
    df["month"]         = df["datetime"].dt.tz_localize(None).dt.to_period("M")
    df["hour"]          = df["datetime"].dt.hour
    df["shift"]         = pd.cut(df["hour"], bins=[-1, 5, 11, 17, 23], labels=["Night", "Morning", "Afternoon", "Evening"])


    accepted            = df[df["verdict"] == "OK"]
    unique_accepted     = accepted.drop_duplicates(subset=["problem_id"]).copy()
    unique_attempted    = df.drop_duplicates(subset=["problem_id"])

    unique_accepted_cnt = len(unique_accepted)
    unique_attempted_cnt= len(unique_attempted)

    solved_by_rating    = unique_accepted["problem_rating"].dropna().value_counts().to_dict()
    attempted_by_rating = unique_attempted["problem_rating"].dropna().value_counts().to_dict()

    avg_solved_rating   = unique_accepted["problem_rating"].dropna().mean()
    highest_sol_rating  = int(unique_accepted["problem_rating"].max())
    lowest_solved_rating= int(unique_accepted["problem_rating"].min())

    unique_accepted["tags"] = unique_accepted["problem"].apply(lambda x: x.get("tags", []))
    tag_count = (
        unique_accepted["tags"]
        .explode()
        .value_counts()
        .to_dict()
    )

    ac_rate_by_rating = (
        df.dropna(subset=["problem_rating"])
        .groupby("problem_rating")["verdict"]
        .apply(lambda x: (x == "OK").mean() * 100)
        .round(2)
        .to_dict()
    )

    avg_attempts_to_solve = round(unique_accepted["attempts"].mean(), 2)
    
    shift_count     = (df.groupby("shift", observed=True)["verdict"].count().to_dict())
    ac_shift_count  = (unique_accepted.groupby("shift", observed=True)["verdict"].count().to_dict())

    ac_rate_shift = {
        shift: round((ac_shift_count.get(shift, 0) / count) * 100, 2)
        if count else 0
        for shift, count in shift_count.items()
    }

    monthly_submissions_grp     = df.groupby("month")
    monthly_unique_ac_grp       = unique_accepted.groupby("month")
    monthly_unique_attempt_grp  = unique_attempted.groupby("month")

    total_submissions_monthly   = monthly_submissions_grp   ["verdict"].count().to_dict()
    unique_accepted_monthly     = monthly_unique_ac_grp     ["verdict"].count().to_dict()
    unique_attempted_monthly    = monthly_unique_attempt_grp["verdict"].count().to_dict()

    ac_rate_monthly = {
        month: round((unique_accepted_monthly.get(month, 0) / count) * 100, 2)
        if count else 0
        for month, count in total_submissions_monthly.items()
    }

    monthly_avg_attempts_to_solve   = round(monthly_unique_ac_grp["attempts"].mean(), 2).to_dict()
    monthly_avg_rating_solved       = monthly_unique_ac_grp["problem_rating"].mean().astype(int).to_dict()

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
        "verdict_count"     : verdict_count, 
        "count"             : len(df), 
        "lang"              : m_lang,
        "unique_attempt"    : unique_attempted_cnt,
        "unique_ac"         : unique_accepted_cnt,
        "attempt_rating"    : attempted_by_rating,
        "solved_rating"     : solved_by_rating,
        "avg_sol_rating"    : int(avg_solved_rating),
        "hi_sol_rating"     : highest_sol_rating,
        "lo_sol_rating"     : lowest_solved_rating,
        "ac_rate_rating"    : ac_rate_by_rating,
        "avg_attempts"      : avg_attempts_to_solve,
        "tag_count"         : tag_count,
        "shift_count"       : shift_count,
        "ac_shift_count"    : ac_shift_count,
        "ac_rate_shift"     : ac_rate_shift,
        "m_submissions"     : total_submissions_monthly,
        "m_ac_submissions"  : unique_accepted_monthly,
        "m_att_submissions" : unique_attempted_monthly,
        "m_ac_rate"         : ac_rate_monthly,
        "m_avg_attempts"    : monthly_avg_attempts_to_solve,
        "m_avg_rating_sol"  : monthly_avg_rating_solved,
    }

    if(opt == 1):
        print2(data2)

    return data2