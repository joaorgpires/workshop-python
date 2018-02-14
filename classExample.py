import operator


class Trick(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "Trick({0:>s})".format(self.__str__())

    def __str__(self):
        return str(self.name) + "," + str(self.score)

    def __eq__(self, other):
        if self.name == other.name and self.score == other.score:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(repr(self))


class Dog(object):
    def __init__(self, kind, name=None, chipnumber=None):
        self.kind = kind
        self.name = name
        self.tricks = set([])
        self._chipnumber = chipnumber

    def __repr__(self):
        return "Dog({0:>s})".format(self.__str__())

    def __str__(self):
        if self.name is not None:
            return str(self.kind) + "," + str(self.name)
        return str(self.kind)

    def __eq__(self, other):
        if self._chipnumber is not None and other._chipnumber is not None:
            return self._chipnumber == other._chipnumber
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(repr(self))

    def addchipnumber(self, chipnumber):
        if self._chipnumber is not None:
            raise ValueError("Dog already has a chipnumber")
        else:
            self._chipnumber = chipnumber

    def addtrick(self, trick):
        self.tricks.add(trick)

    def gettricks(self):
        t = []
        for trick in list(self.tricks):
            t.append(trick.name)
        return set(t)


class Competition(object):
    def __init__(self):
        self.participants = {}
        self._table = {1: None, 2: None, 3: None}
        self._tricks = {}

    def __repr__(self):
        return "Competition({0:>s})".format(self.__str__())

    def __str__(self):
        ans = {}
        for set_key in self.participants:
            ans[set_key] = list(self.participants[set_key])

        return str(ans)

    def addparticipant(self, participant):
        if participant._chipnumber is None:
            raise AttributeError("Participant does not have a chipnumber!")
        elif participant.kind not in self.participants:
            self.participants[participant.kind] = {participant}
        elif participant in self.participants[participant.kind]:
            raise ValueError("Participant already competing!")
        else:
            self.participants[participant.kind].\
                add(participant)

    def podium(self):
        if self._table[1] is None:
            print "No winner yet"
        elif self._table[2] is None:
            print "First Place:  {} with {} point(s)".format(self._table[1][0].name, self._table[1][1])
        elif self._table[3] is None:
            print "First Place:  {} with {} point(s)".format(self._table[1][0].name, self._table[1][1])
            print "Second Place: {} with {} point(s)".format(self._table[2][0].name, self._table[2][1])
        else:
            print "First Place:  {} with {} point(s)".format(self._table[1][0].name, self._table[1][1])
            print "Second Place: {} with {} point(s)".format(self._table[2][0].name, self._table[2][1])
            print "Third Place:  {} with {} point(s)".format(self._table[3][0].name, self._table[3][1])

    def addtrick(self, trick):
        if trick.name in self._tricks:
            raise ValueError("This is already a trick for this competition!")
        else:
            self._tricks[trick.name] = trick.score

    def simulate(self, debug=False):
        tablelist = []
        for kind in self.participants:
            for dog in self.participants[kind]:
                score = 0
                tricks = dog.gettricks()
                for trick in tricks:
                    if trick in self._tricks:
                        score += self._tricks[trick]
                tablelist.append((dog, score))
        sorted_table = sorted(tablelist, key=operator.itemgetter(1), reverse=True)
        it = 1
        for (dog, score) in sorted_table:
            self._table[it] = (dog, score)
            it += 1
        if debug:
            for (dog, _) in sorted_table:
                print dog.name
                it += 1


t1 = Trick("roll over", 1)
t2 = Trick("play dead", 5)
t3 = Trick("roll over", 0)
rufus = Dog("golden retriever", "rufus")
rufus.addchipnumber(1001001)
rufus.addtrick(t1)
rufus.addtrick(t2)
rufus.addtrick(t3)
comp = Competition()
comp.addparticipant(rufus)
kika = Dog("golden retriever", "kika", 1001)
comp.addparticipant(kika)
boy = Dog("portuguese water dog", "boy", 101)
comp.addparticipant(boy)
comp.addtrick(t1)
comp.simulate()
