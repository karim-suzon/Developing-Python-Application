
class House:
    def __init__(self,name):
        self.name = name

    def addRooms(self, r1, r2,r3):
        self.room1 = r1
        self.room2 = r2
        self.room3 = r3
    def getInfo(self):
        print("House name: ", self.name)
        print("Rooms : ")
        print(self.room1.getInfo())
        print(self.room2.getInfo())
        print(self.room3.getInfo())
class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def getInfo(self):
        return self.name + " size is " +str(self.size)

house1 = House("Omakotitalo")
roomA = Room("olohuone", 19)
roomB = Room("makuuhuone", 21)
roomC = Room("vierashuone", 18)
house1.addRooms(roomA,roomB,roomC)
print(roomA.getInfo)
house1.getInfo()
