from apr_abstract_bag_functional import bag_l
from apr_abstract_bag_classes import BagL


def test_bag(b):
    b.add_one('a')
    b.add_one('b')
    b.add_one('c')
    b.add_one('d')
    b.add_one('a')
    b.add_one('b')
    b.add_one('c')
    b.add_one('a')
    b.add_one('b')
    b.remove_one('e')
    b.remove_one('d')
    b.remove_one('d')
    b.remove_one('c')
    b.add_one('a')
    b.add_one('d')
    assert b.number_of('a') == 4
    assert b.number_of('b') == 3
    assert b.number_of('c') == 1
    assert b.number_of('d') == 1
    assert b.number_of('e') == 0
    assert b.number_of('f') == 0
    print('all checked')


def main():
    test_bag(bag_l())
    test_bag(BagL())


if __name__ == '__main__':
    main()
