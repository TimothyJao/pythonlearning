class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUISNESS")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AINT HERE!")

    def __setitem__(self, key, value):
        print("YOU WANT TI CHANGE THE DICTIONARY?")
        print("UGH OK FINE")
        super().__setitem__(key, value)

data = GrumpyDict({"first": "Tim", "animal": "cat"})
print(data)
data['city'] = "Tokyo"
print(data)