#
# Example file for working with classes
#


class MyClass:
    def method1(self):
        print("MyClass method1")

        def method2(self, somestring):
            print("myclass method2", somestring)


class AnotherClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print("anotherClass Method1")

    @staticmethod
    def method2(self, somestring):
        print("anotherClass method2", somestring)


def main():
    c = MyClass()
    c.method1()
    c.method2("this is a string")

    c2 = AnotherClass()
    c2.method1()
    c2.method2()


if __name__ == "__main__":
    main()
