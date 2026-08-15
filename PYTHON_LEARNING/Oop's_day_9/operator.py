class point:
 def __init__(self,x,y):
  self.x = x
  self.y = y
 
 def sum(self, p):
  return point((self.x+p.x) ,  (self.y + p.y))
 
 def print_point(self):
  return f"x is {self.x} and y is {self.y}"

p1 = point(3,2)
p2 = point(6,3) 
p = p1.sum(p2)
print(p.print_point())