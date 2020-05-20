def build_matrix():
    return [ [ 1 if item_idx == row_idx else 0 for item_idx in range(0, 3) ] for row_idx in range(0, 3) ]


def construct_new_list(names):
    return {name[0].upper() + name[1:].lower() for name in names if len(name) > 1}


def construct_new_dict(dict1):
    return {'even': [k for k,v in dict1.items() if v%2==0], 'odd': [k for k,v in dict1.items() if v%2!=0]}


def logger(func):
    def inner(*args, **kwargs):
        print(func.__name__ + ': start')
        func(*args, **kwargs)
        print(func.__name__ + ': end')
    return inner


@logger
def printer(msg):
    print(msg)


def factory(args):
         def int_sum():
            return sum(args)
         def str_sum():
            return ''.join(args)
         def mix_sum():
            return ''.join([str(a) for a in args])
         types = {type(a) for a in args}
         if len(types) == 1:
            return int_sum if types == {int} else str_sum
         return mix_sum


def get_lengths(input_list):
    for person in input_list:
        yield len(person)


if __name__ == "__main__":
    print('#1')
    print(build_matrix())
    print('#2')
    print(construct_new_list([ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]))
    print('#3')
    print(construct_new_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}))
    print('#4')
    printer("Hello")
    print('#5-1')
    sum_method = factory(['m', '2', 3])
    print(sum_method())
    print('#5-2')
    sum_method = factory([1, 2, 3])
    print(sum_method())
    print('#6')
    lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
    for value in get_lengths(lannister):
        print(value)
    print('#7')
    lengths = (len(item) for item in lannister)
    for value in lengths:
        print(value)

