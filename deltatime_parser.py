import re


def delta_time_parser(txt):
    return sum(
        {"y": 31557600, "d": 86400, "h": 3600, "m": 60, "s": 1}[t] * int(a)
        for a, t in re.findall("(\d+)(.)", txt.lower())
    )
