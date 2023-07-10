a = input("Enter a string here : ")
b = str(input("Enter a letter here : "))

if len(b) > 1:
    print("b should only have 1 charecter")
    exit()

counter = 0
for i in a:
    if i == b:
        counter += 1

print(f"The number of {b}'s in your string is {counter}")