from Vehicle import Vehicle 
class Bike(Vehicle):
 def __init__(self):
  print("this is a bike")
def Bike_call(): 
 c1 = Bike()
 print(c1.vehiclenumber("RJ45GGS$$$$"))
 print(c1.brand("HONDA"))
 print(c1.model("CH@892"))
 print(c1.price("22,300"))
 print(c1.speed("140 km/h"))
 print(c1.fueltype("Diesel"))

