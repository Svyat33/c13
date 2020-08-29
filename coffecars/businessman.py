from coffecars import CofeCar, Drink
from typing import List

from coffecars.coord import Coord


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

    def filterCofeCars(self, values: dict) -> List[CofeCar]:

        def getFilter():
            if values.get("address"):
                def get_address(car):
                    if values.get("address").lower() in car.address.lower():
                        return True
                    else:
                        return False
                return get_address
            elif values.get("coord"):  # {"x": 1, "y": 2, "radius": 100}
                def get_coord(car):
                    coord = Coord(values.get("coord").get("x"), values.get("coord").get("y"))
                    distance = coord.distance_to(car.coord)
                    radius = values.get("coord").get("radius")
                    if distance <= radius:
                        return True
                    else:
                        return False
                return get_coord
        return [car for car in self.cofe_cars if getFilter()(car)]



    def filterDrinks(self, name) -> List[Drink]:
        return []

    def applyDrinkstoCar(self, drinks: Drink, cars: List[CofeCar], flag):
        for car in cars:
            car.applyDrinks(drinks, flag)
