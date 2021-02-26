# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
# Ignore letter case.


def is_isogram(string):
    my_string = string.lower()
    if not my_string:
        return True

    check_list = []

    for i in my_string:
        if i.isalpha():
            if i in check_list:
                return False
            check_list.append(i)
        return False
    return True
