
class Group:
    def __init__(self,name):
        self.name = name

    def addMembers(self,m1, m2,m3):
        self.member1 = m1
        self.member2 = m2
        self.member3 = m3
    def getInfo(self):
        print("Group name: ", self.name)
        print("Members : ")
        print(self.member1.getInfo())
        print(self.member2.getInfo())
        print(self.member3.getInfo())
class Member:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    def getInfo(self):
        return self.name + "born in " +str(self.birth_year)

group1 = Group("NUmber1")
memberA = Member("karim", 1988)
memberB = Member("suzon", 1992)
memberC = Member("Abdul", 1991)
group1.addMembers(memberA,memberB,memberC)
print(memberA.getInfo)
group1.getInfo()
