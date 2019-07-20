def func(*args):
    import pdb;pdb.set_trace()
    #dir
    return sum(args)


def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


func(1, 2)
