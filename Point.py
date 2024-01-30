from Item import Item
class Point:
    def __init__(self, items: [Item, Item, Item]):
        self.points = items
        self.item = Item("")
    
    #* Add an item in the first free place
    def Add(self, item) -> None:
        for i in range(len(self.points)):
            if self.points[i].id == '_':
                self.points[i] = item
                break
    
    #* Remove an item from the specified index
    def Remove(self, index:int) -> Item:
        temp = self.points[index]
        self.points[index] = self.item
        return temp
    
    def IsEmptyPoint(self) -> bool:
        for item in self.points:
            if item.name != "":
                return False
        return True
    
    def SearchPoint(self) -> [int, Item]:
        for index in range(len(self.points)):
            if self.points[index].name != "":
                return index, self.points[index]
        return -1, None
    
    #* Returns the number of free spaces of the point
    def FreeSpaces(self) -> int:
        count = 0
        for item in self.points:
            if item.id == '_':
                count += 1
        return count