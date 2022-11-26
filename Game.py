listFactory = {
    [["Iron", 1], ["Bronze", 1], ["Aluminum", 2], ["Energy", 2]] : ["CarFactory", 170],
    [["Aluminum", 1], ["Coal", 1]] : ["BicycleFactory", 70],
    [["Bronze", 1], ["Iron", 1], ["Gold", 1], ["Aluminum", 1], ["Energy", 1]] : ["ElectronicsFactory", 110],
    [["Oil", 2]] : ["RubberFactory", 40]
}
 
class Card:
    def __init__(self, name, description):
        self.name=name
        self.description=description

class Resources(Card):
    pass
    def __init__(self, name, description, costC):
        super().__init__(name, description)
        self.costC=costC

class Energy(Resources, Card):
    def __init__(self, name, description, costC):
        super().__init__(name, description, costC)
class Util(Resources, Card):
    def __init__(self, name, description, costC):
        super().__init__(name, description, costC)

class Event(Card):
    def __init__(self, name, description):
        super().__init__(name, description)
        # listAttribute: pair(int, int)
        # 1 if destroy C
        # 2 if destroy money
        # 3 if buff C
        # 4 if buff money
        # 5 if destroy factory >= costC
        # 6 if destroy all factories
        self.listAttribute=[]
        # traverse over listAttribute

class Player:
    def __init__(self, name):
        self.name=name
        self.carbonCurrency=100
        self.money=0
        self.factoryList=[]
        self.cardList=[]

    def play(self, gm):
        while True:
            choice = int(input())
            if choice==1:
                next
                # generate list of possible operations
                # 1. Build a factory using Resources and Energy Currency
                # 2. Cast Energy type resources into Energy Currency
            elif choice==2:
                newCard=gm.drawCard()
                if(type(newCard)==Event):
                    # execute event
                    next
                else:
                    self.cardList.append(newCard)
                break
            


class Factory:
    def __init__(self, name, buffC, buffCoin):
        self.name=name
        self.buffC=buffC
        self.buffCoin=buffCoin


class Game:
    def __init__(self):
        self.players=[]
        self.players.append(Player("Player1"))
        self.players.append(Player("Player2"))
    def play(self):
        for round in range(20):
            for id_turn in range(2):
                self.players[id_turn].play()
