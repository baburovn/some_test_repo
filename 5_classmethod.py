class Vec:
    MIN_COORD = 0
    MAX_COORD = 100


    def __init__(self,var_x ,var_y):
        self.x = 0
        self.y = 0
        if Vec.valdate(var_x) and Vec.valdate(var_y):
            self.x = var_x
            self.y = var_y

    @classmethod
    def valdate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD


    def get_coord(self):
        return self.x, self.y


v1 = Vec(1,11) # True

print(v1.get_coord()) # (1, 50)
