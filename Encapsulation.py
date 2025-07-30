class Person(object):
    def __init__(self, id, name, age):
        self.name=name
        self.id=id
        self.age=age
    def display(self):
        print("The id of the person is :", self.id)
        print("The name of the person is :", self.name)
        print("The age of the person is :", self.age)

p1 =Person(12, "Rani", 32)
p2 =Person(13, "Anu", 29 )
p1.display()
p2.display()

