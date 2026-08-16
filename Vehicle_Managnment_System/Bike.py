from Vehicle_details import Vehicle
class Bike(Vehicle):
    pass
V1 = Bike()
V1.Vfuel("Petrol")
V1.Vprice('1,89,999')
V1.Vmodel('XB223&#')
V1.Vnumberplate('HA67KK!221')
V1.Vname("Ninja")
V1.Vbrand("Suzuki")
def Bike_display():
    print("---------------------")
    V1.show_details()
    print("---------------------")