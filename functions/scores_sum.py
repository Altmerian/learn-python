scores = [200, 456, 350, 100, 234, 678]


def ending_zero_sum(scores_list):
    result = 0
    for score in scores_list:
        if score % 10 == 0:
            result += score
    return result


print(ending_zero_sum(scores))
