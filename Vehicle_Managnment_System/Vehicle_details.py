class Vehicle:
    def Vname(self,name):
        self.name = name
        return name

    def Vbrand(self,brand):
        self.brand = brand
        return brand

    def Vfuel(self,fuel):
        self.fuel = fuel
        return fuel

    def Vprice(self,price):
        self.price = price
        return price

    def Vmodel(self,model):
        self.model = model
        return model

    def Vnumberplate(self,numberplate):
        self.numberplate = numberplate
        return numberplate    
    
    #Function for display
    def show_details(self):
        print(f"No. = {self.numberplate}\nNAME = {self.name}\nBRAND = {self.brand}\nFUEL TYPE = {self.fuel}\nPRICE = {self.price}\nMODEL = {self.model}")
