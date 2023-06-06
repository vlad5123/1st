class Parent1:
    def __init__(self):
        self.attribute1 = "Attribute 1 from Folder1"

    def method1(self):
        print("Method 1 from Folder1")

class Parent2:
    def __init__(self):
        self.attribute2 = "Attribute 2 from Folder2"

    def method2(self):
        print("Method 2 from Folder2")

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        self.attribute3 = "Folder22"

    def method3(self):
        print("Method 3 in Folder22")


child = Child()


print(child.attribute1)
print(child.attribute2)
print(child.attribute3)

child.method1()
child.method2()
child.method3()
