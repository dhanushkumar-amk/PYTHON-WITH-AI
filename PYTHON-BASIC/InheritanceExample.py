
class Mom:
    def shop(self):
        print("Shop")

class Dad:
    def house(self):
        print("i am from dad house")

class Son(Dad, Mom):
    def fact(self):
        print("i am from son")


s = Son()
s.house()
s.shop()
s.fact()


