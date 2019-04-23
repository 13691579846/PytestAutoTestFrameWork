class class1():

    a = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def funs(self):
        class1.funa()
        self.func()
        pass

    @classmethod
    def funa(cls):
        class1.func()

    @staticmethod
    def func():
        print(class1.a)
        # class1.funa()


    @staticmethod
    def fund():
        class1.func()

a = class1('linux', 22)
class1.func()
a.fund()