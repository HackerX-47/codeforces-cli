from cfv2.imports import *


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