def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a nice day!")
    return wrapper

@be_polite
def greet():
    print("My name is Tim.")

@be_polite
def rage():
    print("I HATE YOU!")

greet()
rage()