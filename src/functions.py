from imports import *

def summary(st_dict):

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


def normalize_lang(lang):
    lang = lang.lower()

    if "gnu" in lang or "c++" in lang:
        return "cpp"

    if "c#" in lang:
        return "c#"

    if "go" in lang:
        return "go"

    if "java" in lang:
        return "java"

    if "kotlin" in lang:
        return "kotlin"

    if "javascript" in lang or "node.js" in lang:
        return "js"
    
    if "python" in lang or "pypy" in lang:
        return "python"

    return "others"