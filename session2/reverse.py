class Reverse:
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    # returns an iterator object 
    def __iter__(self):
        return self

    # accesses elements in the container one at a time.
    # When there are no more elements, raises a StopIteration exception which tells the 
    # for loop to terminate
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


if __name__ == "__main__":
    rev = Reverse('spam')
    for char in rev:
        print(char)

