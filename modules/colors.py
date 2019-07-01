from termcolor import colored

# text = colored("HI THERE!", color = "cyan")
# print(text)
# text = colored("HI THERE!", color = "magenta")
# print(text)

text = colored("HI THERE!", color = "cyan", on_color = "on_magenta", attrs=["blink"])
print(text)