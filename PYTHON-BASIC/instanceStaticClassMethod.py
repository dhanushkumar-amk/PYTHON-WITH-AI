class MyClass:

    def instance_method(self):
        print("instance method called")

    @classmethod
    def class_method(cls):
        print("class method called")


    @staticmethod
    def static_method():
        print("static method called")


obj = MyClass()
obj.instance_method()
MyClass.class_method()
MyClass.static_method()