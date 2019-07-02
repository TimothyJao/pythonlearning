class User:

    active_users = 0

    @classmethod
    def display_action_users(cls):
        return "There are currently " + str(cls.active_users) + " active users"
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.active_users += 1
        
    def __repr__(self):
        return self.first_name + " is " + str(self.age)

    def logout(self):
        User.active_users -= 1
        return self.first_name + " has logged out"

    def full_name(self):
        return self.first_name + " " + self.last_name

    def initials(self):
        return self.first_name[0] + "." + self.last_name[0]

    def likes(self, thing):
        return self.first_name + " likes " + thing
    
    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return "Happy " + str(self.age) +"th, "+ self.first_name
    
    def say_hi():
        print("HELLO!!!!")

class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1
    
    def remove_post(self):
        return f"{self.full_name()} remove a post from the {self.community} community"
    
    @classmethod
    def display_action_mods(cls):
        return "There are currently " + str(cls.total_mods) + " active mods"
    

# print(user2.full_name())
# print(user1.initials())
# print(user1.likes("ice cream"))

# print(user1.is_senior())
# print(user2.birthday())

# print(User.active_users)

# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)

# print(User.active_users)

# print(user1.logout())

# print(User.active_users)
# print(User.display_action_users())

# tom = User.from_string("Tom,Jones,89")
# print(tom.first_name)
# print(tom.last_name)
# print(tom.birthday())
# print(tom)
u1 = User("Tom", "Garcia", 35)
u2 = User("Tom", "Garcia", 35)
u3 = User("Tom", "Garcia", 35)
jasmine = Moderator("Jasmine", "O'conner", 61, "Piano")
jasmine2 = Moderator("Jasmine", "O'conner", 61, "Piano")
print(User.display_action_users())
print(Moderator.display_action_mods())
