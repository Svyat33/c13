import pickle

from coffecars.coord import Coord
from coffecars.drink import DrinksList, Drink


class CofeCar:

    NORM_DISTANCE = 20

    '''
    street address
    coord
    drinks_list

    store
    restore
    '''
    def __init__(self, cord, adres):
        self.cord = cord
        self.address = adres
        self.drincs = []

    def add(self, drinc):
        if isinstance(drinc, Drink):
            if drinc not in self.drincs:
                self.drincs.append(drinc)
                drinc.setCar(self)

    @property
    def asdict(self):
        return {'ader': self.address,
                'cord': self.cord.dict_cord,
                'drics':[d.name for d in self.drincs]}

    def restor(self, params, drincs_list: DrinksList):
        self.address = params['ader']
        self.cord = Coord(params['cord']['x'],params['cord']['y'])
        for drink_name in params.get('drics'):
            drink = drincs_list.getDrinkByName(drink_name)
            self.add( drink )

    def __eq__(self, other):
        return isinstance(other, CofeCar) and self.cord.distance_to(other) < CofeCar.NORM_DISTANCE

    def applyDrinks(self, drinks, flag):
        if flag:
            self.remDrinks(None)
        for drink in drinks:
            self.add(drink)

    def remDrinks(self, drinks):
        if not drinks:
            drinks = self.drincs
        for drink in drinks:
            if drink in self.drincs:
                self.drincs.pop(self.drincs.index(drink))
                drink.remCar(self)





class Cars_list:
    def __init__(self):
        self.cars = []

    def serch(self, cord,radius=200):
        pass

    def __len__(self):
        return len(self.cars)

    def print(self):
        pass

    def add(self, car):
        pass

    def search(self, like=""):
        '''
        Отобрать список машин по признаку
        :param like: строка
        :return: лист машин
        '''
        ret = []
        pass #...
        return ret

    def set_drink(self, rcvr=None, drink: Drink=None):
        '''
        Проставить списку машин наличие напитка
        :param rcvr:  список машин
        :param drink:  напиток
        :return:
        '''
        rcvr = rcvr or []

        for car in rcvr:
            car.add(drink)

    def storag(self,file):
        pass

    @classmethod
    def restorag(cls, file, drinks_list):
        ret = cls()

        return ret

