from collections import namedtuple

Bag = namedtuple('Bag', 'add_one remove_one number_of')


def bag_l():
    lst = []

    def add_one(element):
        lst.append(element)

    def remove_one(element):
        try:
            lst.remove(element)
        except ValueError:
            pass

    def number_of(element):
        return lst.count(element)

    return Bag(add_one, remove_one, number_of)
