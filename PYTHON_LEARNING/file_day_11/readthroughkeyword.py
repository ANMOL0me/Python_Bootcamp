'''f = open("dummyfile.txt","r")

content = f.read()
print(content)
f.close()

with open("dummyfile.txt","r") as f:
 content = f.read()
 print(content)
#file is already closed by default'''

try:
    with open("dummyfile.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

with open("output.txt", "w") as file:
    file.write("Data written using 'with'.\n")