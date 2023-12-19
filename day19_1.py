import re

with open("day19_input.txt", "rt") as f:
    inputs = [line.strip() for line in f.readlines()]

dividing_index = inputs.index("")
workflows = inputs[:dividing_index]
part_ratings = inputs[dividing_index + 1 :]


def get_part_rating(part_rating_str: str) -> str:
    matchings = re.match(
        r"\{x=(\d+)\,m=(\d+)\,a=(\d+)\,s=(\d+)\}", part_rating_str
    ).groups()
    return {
        "x": int(matchings[0]),
        "m": int(matchings[1]),
        "a": int(matchings[2]),
        "s": int(matchings[3]),
    }


def get_workflow(workflow_str: str) -> (str, callable):
    parts = re.match(
        r"(?P<name>\w*)\{(?P<pattern>([xmas][\<\>]\d*\:\w*\,)+)(?P<elsename>\w*)\}",
        workflow_str,
    )
    patterns = parts.group("pattern")[:-1].split(",")

    def return_func(part_rating: dict) -> str:
        for pattern in patterns:
            pattern_parts = re.match(
                r"(?P<category>[xmas])(?P<operator>[\<\>])(?P<val>\d*)\:(?P<res>\w*)",
                pattern,
            )
            category = part_rating[pattern_parts.group("category")]
            operator = pattern_parts.group("operator")
            res = pattern_parts.group("res")
            val = int(pattern_parts.group("val"))
            if operator == "<":
                if category < val:
                    return res
                else:
                    pass
            elif operator == ">":
                if category > val:
                    return res
                else:
                    pass
        return parts.group("elsename")

    return parts.group("name"), return_func


part_ratings = [get_part_rating(part_rating) for part_rating in part_ratings]
workflows = {
    get_workflow(workflow)[0]: get_workflow(workflow)[1] for workflow in workflows
}


rating_sum = 0
for part_rating in part_ratings:
    flow = workflows["in"](part_rating)
    while flow not in ["R", "A"]:
        flow = workflows[flow](part_rating)

    if flow == "A":
        rating_sum += (
            part_rating["x"] + part_rating["m"] + part_rating["a"] + part_rating["s"]
        )

print(rating_sum)
