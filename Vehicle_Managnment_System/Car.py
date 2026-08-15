from Vehicle import Vehicle 
class Car(Vehicle):
 def __init__(self):
  print("this is a car")
def car_call(): 
 c1 = Car()
 print(c1.vehiclenumber("RJ14XS$$$$"))
 print(c1.brand("NANO"))
 print(c1.model("CH@@332"))
 print(c1.price("232,300"))
 print(c1.speed("140 km/h"))
 print(c1.fueltype("Petrol"))
