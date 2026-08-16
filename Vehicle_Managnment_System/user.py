import Car
import Bike
while True:
    inp = input("1. Car details\n2. Bike details\n")
    if inp=="1":
        Car.car_display()
    elif inp=="2":
        Bike.Bike_display()
    else:
        print(f"Check your input {inp}")
        break    