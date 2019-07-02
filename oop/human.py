class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def full_name(self):
        return self.first + " " + self.last

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")
    

jane = Human("Jane", "Goodall", 50)
print(jane.age)
jane.age = 20
print(jane.age)
print(jane.full_name)
jane.full_name = "Tim Minchin"
print(jane.full_name)