#case changing

text = "  Python hello  "
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

#remove whitespace
#text = "hello world"
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#Finding and Replacing
print(text.find("hello"))
print(text.replace("hello","world"))

#splitting and joining
txt = "apple.banana,mango"
fruits = text.split(",")
print(fruits)
