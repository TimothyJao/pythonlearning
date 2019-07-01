def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Don't divide by zero please!")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided {b} is {result}")

divide(1,2)
divide(1,'a')