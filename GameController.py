from Item import Item
from Boat import Boat
from Point import Point
import os, time

class GameController:
    def __init__(self):
        self.lap = 0
        self.begin = True
        self.pointA = Point([Item(""),Item(""),Item("")])
        self.pointB = Point([Item(""),Item(""),Item("")])
        self.boat = Boat(Item(""))
        self.item = Item("")
    
    #* Initialize game by placing the items at point A
    #* Fox eats chicken, chicken eats wheat
    def InitGame(self) -> None:
        self.pointA.Add(Item("fox", 'f', 'c'))
        self.pointA.Add(Item("chicken", 'c', 'w'))
        self.pointA.Add(Item("wheat", 'w'))

    def Start(self) -> None:
        self.InitGame()
        while True:
            self.ShowMap()
            point = self.boat.Movement()
            if point == 'a':
                self.ParkA()
                self.SetLap()
            elif point == 'b':
                self.ParkB()
                self.SetLap()
            time.sleep(1)
            if self.IsGameOver():
                self.ShowMap()
                print("Laps: " + str(self.lap))
                break

    #* Check if any of the items eat the other
    def Check1of3(self, list: [Item, Item]) -> bool:
        for it in range(len(list)):
            for food in range(len(list)):
                if list[food] != '_' and list[it] != '_':
                    if list[it].eat == list[food].id:
                        return False
        return True

    #* Check if one item eats the other
    def IsThereAProblem(self, itemOnBoard: Item, itemInList: Item) -> bool:
        if itemOnBoard.eat == itemInList.id or itemInList.eat == itemOnBoard.id:
            return True
        return False

    def ParkA(self) -> None:
        index = -1
        # Boat has free space
        if self.boat.boat[1].id == '_':
            # Take an item and check if there is a problem
            for item in range(len(self.pointA.points)):
                if self.pointA.points[item].id != '_':
                    tempItem = self.pointA.points[item]
                    tempList = self.pointA.points.copy()
                    tempList.remove(tempItem)
                    # Select the one that does not cause danger
                    if self.Check1of3(tempList):
                        index = item
                        break
            if index > -1:
                    self.boat.GetInBoat(self.pointA.Remove(index))
        # There is an item in the boat
        else:
            # Search a free space in point A
            index, search = self.pointA.SearchPoint()
            # If you place the item in Point A and there is a problem? -> change them
            if self.IsThereAProblem(self.boat.boat[1], search) == True:
                self.pointA.Add(self.boat.GetOutBoat())
                self.boat.GetInBoat(self.pointA.Remove(index))

    def ParkB(self) -> None:
        if self.pointB.IsEmptyPoint():
            self.pointB.Add(self.boat.GetOutBoat())
        else:
            index, search = self.pointB.SearchPoint()
            # There is more than just 1 free space
            if self.pointB.FreeSpaces() > 1:
                # If you place the item in Point B and there is a problem? -> change them
                if self.IsThereAProblem(self.boat.boat[1], search) == True:
                    self.pointB.Add(self.boat.GetOutBoat())
                    self.boat.GetInBoat(self.pointB.Remove(index))
                else:
                    self.pointB.Add(self.boat.GetOutBoat())
            # Is the last free space
            else:
                self.pointB.Add(self.boat.GetOutBoat())

    def ShowMap(self) -> None:
        os.system("clear")
        print("\tLAP: " + str(self.lap) + "\n")
        for i in range(3):    
            print(self.pointA.points[i], end='')
            if(i == 0):
                # \t times boatSpace to animate the movement
                print("\t"*self.boat.spaceA, end='')
                print(self.boat, end='')
                print("\t"*(self.boat.spaceB+1), end='')
            else:
                print("\t\t\t", end='')
            print(self.pointB.points[i])

    def SetLap(self) -> None:
        if self.begin == False:
            self.lap += 1
        else:
            self.begin = False

    def IsGameOver(self) -> bool:
        if self.pointB.FreeSpaces() == 0:
            return True
        return False