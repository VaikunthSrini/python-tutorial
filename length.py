a = str(input("Enter a string : "))

counter = 0

for i in a:
    if i != " ":
        counter += 1

print(counter)