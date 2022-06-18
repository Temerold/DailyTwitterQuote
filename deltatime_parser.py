import yaml
import re

with open("auth.yml", "r") as file:
    yml_config = yaml.safe_load(file)["sus"]
    print(yml_config)  # ! debug!!


def delta_time_parser(txt):
    return sum(
        {"y": 31557600, "d": 86400, "h": 3600, "m": 60, "s": 1}[t] * int(a)
        for a, t in re.findall("(\d+)(.)", txt.lower())
    )


print(delta_time_parser("1H"))
