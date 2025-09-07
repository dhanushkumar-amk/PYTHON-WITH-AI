class dad:
    def factory(self):
        print("i have factory and its color red")

class mom:
    def shop(self):
        print("i have shop and its color green")


class Son(dad, mom):
    def factory(self):
        print("i have factory and i modified as a color : blue")


son = Son()
son.factory()
son.shop()

