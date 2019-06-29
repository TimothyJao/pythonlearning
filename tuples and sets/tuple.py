#Tuples are commonly used for UNCHANGING data:
months = ('January', "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

for month in months:
    print(month)

i = len(months)-1
while i >= 0:
    print(months[i])
    i -= 1
#Tuples can be used as keys in dictionaries:
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office",
} 