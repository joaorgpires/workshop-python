class MyList(object):
    def __init__(self):
        self.lst = []
        self.typeOfMyList = type(None)

    def __repr__(self):
        return "MyList({})".format(str(self))

    def __str__(self):
        return str(self.lst)

    def getsize(self):
        return len(self.lst)

    def summyelements(self):
        pass

    def addelement(self, item):
        if type(item) is not self.typeOfMyList:
            raise TypeError("This item is not an " + str(self.typeOfMyList) + "!")
        else:
            self.lst.append(item)


class MyIntList(MyList):
    def __init__(self):
        super(MyIntList, self).__init__()
        self.typeOfMyList = type(42)

    def summyelements(self):
        ans = 0
        for item in self.lst:
            ans += item
        return ans


class MyStringList(MyList):
    def __init__(self):
        super(MyStringList, self).__init__()
        self.typeOfMyList = type("42")

    def summyelements(self):
        ans = ""
        for item in self.lst:
            ans += item + "."
        return ans
