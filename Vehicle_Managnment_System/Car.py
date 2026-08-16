from Vehicle_details import Vehicle
class Car(Vehicle):
    pass
V1 = Car()
V1.Vfuel("Petrol")
V1.Vprice('2,33,499')
V1.Vmodel('2,33,499')
V1.Vnumberplate('2,33,499')
V1.Vname("ALTO")
V1.Vbrand("Suzuki")
def car_display():
    V1.show_details()