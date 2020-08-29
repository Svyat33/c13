from coffecars import CofeCar, Drink
from typing import List


class BusinessOwner:
    def __init__(self, name=""):
        self.name = name
        self.cofe_cars = []
        self.drinks_list = []

    def addCofeCar(self):
        pass

    def remCofeCar(self):
        pass

    def addDrinks(self):
        pass

    def remDrinks(self):
        pass

    def filterCofeCars(self, adress) -> List[CofeCar]:
        return []

    def filterDrinks(self, name) -> List[Drink]:
        return []

    def applyDrinkstoCar(self, drinks: Drink, cars: CofeCar, flag):
        for car in cars:
            pass
