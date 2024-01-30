from Item import Item
class Boat:
    def __init__(self, item):
        # default
        self.boat = ['R', item]
        self.item = Item("")
        
        # movement
        self.spaceA = 1
        self.changeA = False
        self.spaceB = 1
        self.changeB = True

    def GetInBoat(self, item) -> None:
        self.boat[1] = item

    def GetOutBoat(self) -> str:
        temp = self.boat[1]
        self.boat[1] = self.item
        return temp

    #* Number of spaces between the boat and each point
    #* When you get to a point, update the current point
    def Movement(self) -> str:
        point = ''
        if self.changeA:
            self.spaceA += 1
            if self.spaceA == 2:
                self.changeA = False
        else:
            self.spaceA -= 1
            if self.spaceA == 0:
                self.changeA = True
                point = 'a'
        if self.changeB:
            self.spaceB += 1
            if self.spaceB == 2:
                self.changeB = False
        else:
            self.spaceB -= 1
            if self.spaceB == 0:
                self.changeB = True
                point = 'b'
        return point
    
    def __str__(self) -> str:
        return "["+self.boat[0]+"."+str(self.boat[1])+"]"