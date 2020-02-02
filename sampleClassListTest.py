#
#
#
# The Sample Class Test of List Using


class ClassFamily(object):
    def __init__(self, listData):
        self.data =listData

    def intGetLenth(self):
       # print(len(self.data))
        return len(self.data)
    def printFamilyLenth(self):
        print("My Family have %d Members!"%self.intGetLenth())

    def printFamilyMember(self):
        for self.strName in self.data:
            print("My Family member has: %s" % self.strName)


listMyFamily = ["AddyXiao", "EleaZhao", "ClerkXiao"]
MyFamily = ClassFamily(listMyFamily)
MyFamily.printFamilyLenth()
MyFamily.printFamilyMember()
