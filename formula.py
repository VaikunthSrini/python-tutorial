import unicodedata

a = str(input("you can figure ot the formula of the se shapes: triangle, rectangle, circle. just type the one that you want : "))

if a == "triangle":
    print("(l * w) / 2")

if a == "rectangle":
    print("l * w")

if a == "circle":
    print(unicodedata.lookup("GREEK SMALL LETTER PI") + "r ^ 2")