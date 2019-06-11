# with connect("db") as conn:
#     cur = conn.cursor()
#     cur.execute("create table temp")
#
#     # Do some work
#
#     cur.execute("drop table temp")

# print("create table")
# print("drop table")


class temptable:
    def __init__(self):
        pass

    def __enter__(self):
        print("create table temp")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("drop table temp")


# with temptable():
#     pass


def temptable2():
    print("create table temp 2 ")
    yield
    print("drop table temp 2 ")


class contextmanager:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        self.gen = temptable2()
        next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        next(self.gen, None)


# temptable2 = contextmanager(temptable2)
# with temptable2:
#     pass


from contextlib import contextmanager


@contextmanager
def temptable3():
    print("create table temp 3 ")
    try:
        yield
    finally:
        print("drop table temp 3 ")


with temptable3():
    pass
