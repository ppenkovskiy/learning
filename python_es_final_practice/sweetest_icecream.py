class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles


def sweetest_icecream(lst):
    my_dict = {'Plain': 0,
               'Vanilla': 5,
               'ChocolateChip': 5,
               'Strawberry': 10,
               'Chocolate': 10}
    res = 0
    for l in lst:
        l_res = my_dict[l.flavor] + l.sprinkles
        if l_res > res:
            res = l_res
    return res
