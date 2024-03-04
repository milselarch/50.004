def is_valid_lcs(str1, str2):
    k = 0
    i = 0

    if len(str2) > len(str1):
        return False

    try:
        while (k < len(str1)) and (i < len(str2)):
            # print('POP', (k, i), str1[k], str2[i])
            while str1[k] != str2[i]:
                # print('INC', (k, i), str1[k], str2[i])
                k += 1

            i += 1
    except IndexError:
        return False

    if k >= len(str1):
        return False

    return True


if __name__ == '__main__':
    print(is_valid_lcs('acre', 'ace'))
    print(is_valid_lcs('acer', 'ace'))
    print(is_valid_lcs('acer', 'aceq'))