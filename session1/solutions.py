def upper_lower_counter(str):
    upper_case = 0
    lower_case = 0
    for char in str:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        else:
            pass
    print("Original String : ", str)
    print("No. of Upper case characters : ", upper_case)
    print("No. of Lower case Characters : ", lower_case)


def unique_list_1(lst):
    return list(set(lst))


def unique_list_2(lst):
    unique = []
    for item in lst:
        item not in unique and unique.append(item)
    return unique


def backwords_list(lst):
    return ' '.join(lst[::-1])


def is_palindrome_1(s):
    return s == s[::-1]


def is_palindrome_2(test_str):
    left_pos = 0
    right_pos = len(test_str) - 1

    while right_pos >= left_pos:
        if not test_str[left_pos] == test_str[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


def from_list_to_num(numbers):
    str_num = []
    for num in numbers:
        str_num.append(str(num))
    print(int("".join(str_num)))


def find_equal_and_diff_of_two_lists(list1, list2):
    print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
    print('Additional values in second list: ', ','.join(set(list2).difference(list1)))


def match_items_in_dicts(dict1, dict2):
    for (key, value) in set(dict1.items()) & set(dict2.items()):
        print(f'{key}: {value} is present in both dictionaries')


def backwards_string(str):
    words = str.split(' ')
    words.reverse()
    print(' '.join(words))


def dict_compare(dict1, dict2):
    d1_keys = set(dict1.keys())
    d2_keys = set(dict2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {}
    for obj in intersect_keys:
        if dict1[obj] != dict2[obj]:
            modified[obj] = (dict1[obj], dict2[obj])
    same = []
    for obj in intersect_keys:
        if dict1[obj] == dict2[obj]:
            same.append(obj)
    print('added: ', added)
    print('removed:', removed)
    print('modified: ', modified)
    print('same: ', same)


if __name__ == "__main__":
    upper_lower_counter('The quick Brown Fox')
    print(unique_list_1([1, 2, 3, 3, 3, 3, 4, 5]))
    print(is_palindrome_1('bazab'))
    match_items_in_dicts({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2})
    from_list_to_num([11, 33, 77])
    find_equal_and_diff_of_two_lists(list1=['a', 'b', 'c', 'd', 'e', 'f'],
                                     list2=['d', 'e', 'f', 'g', 'h'])
    backwards_string('My name is Keren')
    dict_compare({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 3, 'd': 4})
