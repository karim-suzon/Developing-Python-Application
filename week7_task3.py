#3.Bird has features name and amount of eggs.
# Amount of eggs has to be between 1 and 10.

#Migratory has special features:
#there is attribute named country that is the destination country and month when the migration mainly occurs.
#Country name has to begin with a cap and its length has to be
#between 5 to 20. Month has to be between 1 and 12.

class Bird:
    def setName(self,n):
        self.__name = n
    def getName(self):
        return self.__name
    def setEggs(self, e):
        self.__eggs = e
    def getEggs(self):
        return self.__eggs
    def display(self):
        e = 10
        if e <= 10:

            print("Name: ", self.getName())
            print("Eggs :", self.getEggs())

b = Bird()
b.setName('duck')
b.setEggs(12)
b.display()
