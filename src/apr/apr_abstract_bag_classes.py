class Bag:
    def add_one(self, element):
        pass

    def remove_one(self, element):
        pass

    def number_of(self, element):
        pass


class BagL(Bag):
    def __init__(self):
        self._lst = []

    def add_one(self, element):
        self._lst.append(element)

    def remove_one(self, element):
        try:
            self._lst.remove(element)
        except ValueError:
            pass

    def number_of(self, element):
        return self._lst.count(element)
