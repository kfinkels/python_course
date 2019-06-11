from time import sleep


def process(file):
    result = []
    with open(file) as f:
        for line in f.readlines():
            result.append(line.lower())
            sleep(0.5)
    return result


for line in process("file2.csv"):
    print(line)

# for x in y:
#     pass
#
# xi = iter(y)
# while True:
#     x = xi.next()


class Process:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        self.f = open(self.file)
        return self

    def __next__(self):
        line = self.f.readline()

        if not line:
            raise StopIteration

        sleep(0.5)
        return line

#
# for line in Process("file2.csv"):
#     print(line)


def process2(file):
    with open(file) as f:
        for line in f.readlines():
            sleep(0.5)
            yield line


# for line in process2("file2.csv"):
#     print(line)
