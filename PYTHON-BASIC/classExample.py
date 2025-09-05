class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello {self.name} and I am {self.age} years old.")


student = Student("dhanushkumar", 21)
student.say_hello()


class StudentDetails:
    def __init__(self, rollNO, className):
        self.rollNO = rollNO
        self.className = className


    def getStudentInfo(self):
        print(f"student roll no: {self.rollNO} and class name: {self.className}")


studentDetails = StudentDetails(rollNO=21, className="Python")
studentDetails.getStudentInfo()