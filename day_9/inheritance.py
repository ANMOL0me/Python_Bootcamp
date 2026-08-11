class animal:#parent class
 name = "kkk"
 def __init__(self,name):
  self.name = name
 def speak(self):
  print(""sound of animal)
class dog(animal):
 def speak(self):
  print("woof!")
d = dog
d.speak()
d.speak(animal)