class Parent:
    def __init__(self):
        self.public_variable = "i am public_variable"
        self._protected_variable = "i am protected_variable"
        self.__private_variable = "i am private_variable"


    def access_from_same_class(self):
        print("Inside the parent class")
        print("public variable is : ", self.public_variable)
        print("protected variable is : ", self._protected_variable)
        print("Private Variable is : ", self.__private_variable)


class Child(Parent):
    def acess_from_sub_Class(self):
        print("Inside the child class")
        print("public variable is : ", self.public_variable)
        print("protected variable is : ", self._protected_variable)

        try:
            print("Private variable is : ", self.__private_variable)
        except AttributeError:
            print("Private : ❌  cannot access private variable")



p = Parent()
p.access_from_same_class()

c = Child()
c.acess_from_subClass()