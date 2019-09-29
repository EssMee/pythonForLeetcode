class stringReverse:
    def __init__(self, string):
        self.string = string 
        self.index = len(string)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration("stop")
        self.index -= 1
        return self.string[self.index]

for c in stringReverse("python"):
    print(c)
