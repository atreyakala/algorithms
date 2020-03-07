class Queue:
    def __init__(self, inp = [], out = []):
        self.inp = inp
        self.out = out

    def push(self, val):
        self.inp.append(val)

    def pop(self):
        if len(self.out) == 0:
            self.shift(self.inp, self.out)
        return self.out.pop()

    def peek(self):
        if len(self.out) == 0:
            self.shift(inp, out)
        return self.out[-1]

    def empty(self):
        return len(self.inp) == 0 and len(self.out) == 0

    def shift(self, source, destination):
        while(len(source) > 0):
            destination.append(source.pop())
