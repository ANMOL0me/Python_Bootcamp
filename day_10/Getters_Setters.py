'''class Brand:
 def __init__(self,name,amt):
  self.name = name
  self.amt = amt
 def fname(self):
  l  = self.name.split(" ")
  print(l)
  return l[0]

e = Brand("Jack Daniels",3400)
print(e.fname())'''



h = "I am going to home"
k = h.split(" ")
print(k)
for i in range(3):
 print(k[i])
##['I', 'am', 'going', 'to', 'home']