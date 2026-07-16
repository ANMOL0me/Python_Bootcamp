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

new_txt = " - ".join(fruits)
print(new_txt)


#string properties
 
str = "python123"
print(str.isalpha())
print(str.isdigit())
print(str.isalnum())
print(str.isspace())

# length
charac = "hello , python"
print(len(charac))
print(ord('A'))
print(charac(65))
