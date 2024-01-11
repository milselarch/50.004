import random


def rand_string(min_length=5, max_length=12):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    assert max_length >= min_length
    max_span = max_length - min_length
    span = random.randint(0, max_span)

    length = min_length + span
    string = ''.join([
        random.choice(chars) for k in range(length)
    ])
    return string


def string_cmp(a, b):
    """
    returns longest
    """
    match_length = 0
    search_length = min(len(a), len(b))

    for k in range(search_length):
        if a[k] == b[k]:
            match_length += 1
        else:
            break

    return match_length


def match_array(a, b):
    """
    generate a 2D array c
    where c[k][i] represents the length of the longest starting
    substring that is shared between a[:k] and b[:i] that is
    at the start of both strings
    xkhopxlktk pdwohjlzjk
    """
    match_counts = []

    for k in range(len(a)):
        match_row = []

        for i in range(len(b)):
            a_substr = a[k:]
            b_substr = b[i:]

            max_match_length = string_cmp(a_substr, b_substr)
            match_row.append(max_match_length)

        match_counts.append(match_row)

    return match_counts


def build_strings(match_arr):
    char_arr_a, char_arr_b = [], []




if __name__ == '__main__':
    """
    for k in range(10):
        a, b = rand_string(), rand_string()
        print(a, b, string_cmp(a, b), match_array(a, b))
    """

    print(match_array('abcde', 'cda'))