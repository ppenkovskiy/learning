def is_full_house(cards):
    flag = True
    for c in cards:
        if cards.count(c) > 3:
            flag = False
    return len(set(cards)) == 2 and flag


print(is_full_house(["A", "A", "A", "K", "K"]))
print(is_full_house(["3", "J", "J", "3", "3"]))
print(is_full_house(["10", "J", "10", "10", "10"]))
print(is_full_house(["7", "J", "3", "4", "2"]))