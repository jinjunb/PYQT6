# @File OOP-test PY.
# @Software:PyCharm
# Created by Dr. Jinjun Bian Email: jinjunbicu@163.com
# @time: 18:47 2023/4/29
import datetime

class Driver:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def drive_car(self, car):
        print(f"司机:{self.name}在开{car}车")
        car.start()

    def __str__(self):
        return  self.name

class Manufacture:
    def __init__(self, name, address):
        self.name =  name
        self.address = address

    def __str__(self):
        return self.name

class Car:
    def __init__(self, brand, model, displacement, production_date, menufacture, price=0.00):
        self.brand = brand
        self.model = model
        self.displacement = displacement
        self.production_date = production_date
        self.price = price
        self.menufacture =  menufacture

    def start(self):
        print(f"{self}汽车启动了。。。")

    def stop(self):
        print(f"{self}汽车停止了。。。")

    def __str__(self):
        return f'{self.brand}:{self.model}'

if __name__ == "__main__":
    d = Driver("Mike",22)
    m = Manufacture("Mercedes-Benz", "Germany")
    c= Car("Benz", "E660", "3.0", datetime.date(2016, 3, 4),m, 250000)
    d.drive_car(c)
    print(c.menufacture.name, c.menufacture.address)


