class sectionc:
 sname = "anmol"


 def show_name(self,sname):
  self.sname = sname  
  print(f"name = {sname}")


 def __init__(self):
  print(f"name={self.sname}")


obj1 = sectionc()#class attribute
obj1.show_name("sfl")#instance attribute
print(dir(obj1))
print(sectionc.sname)
 