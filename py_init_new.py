class Matryoshka:
    def __init__(self, dress_color, eye_color, name):
        print(f"запускается метод __init__ и наделяет эксземпляр типа {self.__class__} переданными х-ми")
        self.dress_color = dress_color
        self.eye_color = eye_color
        self.name = name


    def __new__(cls, *args, **kwargs):
        print(f"запускается метод __new__ и аллоцируется память для хранения экземпляра типа  {cls}")
        res = super().__new__(cls)
        return res

    def say_hello(self):
        print(f"Название текущей матрешки: {self.name} с цветом платья {self.dress_color} и цветом глаз {self.eye_color}")


matr1 = Matryoshka("blu", "red", "Vana")

