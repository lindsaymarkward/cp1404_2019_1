class Thing:
    def __init__(self, x):
        self.x = x

    def area(self):
        pass

    def __len__(self):
        return self.x


class Other(Thing):
    def __init__(self):
        super().__init__(0)
        pass

    def area(self):
        pass


t = Thing(5)

print(len(t))

# t = Thing(3)
# o = Other()
# t.whatever = "Ha?"
#
# t2 = Thing(-1)
#
# print(t.x)
# print(t.whatever)
#
# print(t2.x)
#
# print(o.x)
# "ha".upper()
# str.upper("ha")
