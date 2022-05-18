class EnevLen:
    def eve_len(self):
        return len(self) % 2 == 0


class MyLust(list, EnevLen):
    pass

ml = MyLust([1,2,3,7])
print(ml)