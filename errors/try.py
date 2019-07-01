# try:
#     foobar
# except:
#     print("PROBLEM!")
# print("after the try")

def get(dict, key):
    try:
        return d[key]
    except KeyError:
        return None

d = {"name": "Ricky"}
print(get(d, "city"))
print(get(d, "name"))