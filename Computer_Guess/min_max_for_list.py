def min_list(lst):
    minimum = None
    for num in lst:
        if minimum is None or num < minimum:
            minimum = num
    return minimum


def max_list(lst):
    maximum = None
    for num in lst:
        if maximum is None or num > maximum:
            maximum = num
    return maximum
