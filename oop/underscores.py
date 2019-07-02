# _name use # if you want to make a private attribute but it is just a convention
# __name # name-mangling: to make a method or attribute partiuclar to a class
# __name__ # use if you're overiding a inherit method/attribute

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!"
        self.__msg = "I like turtles"
    # def doorman(self, guess):
    #     if guess == self._secret:
    #         print("Come inside buddy")
    #     else:
    #         print("Wrong password")

p = Person()

print(p.name)
print(p._secret)
# print(p.__msg)
print(p._Person__msg)