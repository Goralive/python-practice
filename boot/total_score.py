def merge(dict1, dict2):
    match = {}
    for first in dict1:
        match[first] = dict1[first]
    for second in dict2:
        match[second] = dict2[second]
    return match


def total_score(score_dict):
    overall = 0
    for score in score_dict:
        overall += score_dict[score]
    return overall


first_half = {"first_quarter": 10, "second_quarter": 20}

second_half = {"third_quarter": 30, "fourth_quarter": 40}

temp = merge(first_half, second_half)

actual_score = total_score(temp)
print(f"Total score should be 100 -> {actual_score}")
