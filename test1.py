# -*- coding: utf-8 -*-

# =============================================================================
# 今有車輛「汽車」和「機車」,請使用物件的繼承介面描述二者相同與差異
# =============================================================================

class Transportation():
    def __init__(self, mileage=None, age=None, oil=None):
        self.mileage = mileage
        self.age = age
        self.oil = oil
        
class Car(Transportation): 
    pass

class Motorcycle(Transportation):
    pass

car = Car(mileage=1000, age=5, oil=300)
moto = Motorcycle(mileage=100, age=1, oil = 50)

print(f'汽車 | 里程數 : {car.mileage} , 車齡 : {car.age} , 機油里程數 : {car.oil}')
print(f'機車 | 里程數 : {moto.mileage} , 車齡 : {moto.age} , 機油里程數 : {car.oil}')


