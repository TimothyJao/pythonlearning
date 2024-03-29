import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored 

header = figlet_format("DAD JOKE 3000")
header = colored(header, color="magenta")
print(header)
term = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers = {"Accept": "application/json"},
    params={"term": term}
).json()

results = res["results"]

num_jokes = res["total_jokes"]
if num_jokes > 1:
    print(f"I found {num_jokes} about {term}. Here's one:")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print("THERE IS ONLY ONE JOKE")
    print(results[0]["joke"])
else:
    print(f"Sorry, I couldn't find a joke with your term: {term}")