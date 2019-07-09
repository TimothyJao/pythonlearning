def eat_junk(food):
    assert food in [
        "pizza", 
        "ice cream", 
        "candy", 
        "fried butter"
        ], "food must be a junk food!"
    return f"NOM NOM NOM I am eating {food}"

food = input("ENTER A FOOD PELASE: ")
print(eat_junk(food))