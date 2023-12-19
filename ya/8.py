from collections import Counter


def diversity(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    common_elements = counter1 & counter2
    return len(list1) + len(list2) - 2 * sum(common_elements.values())


with open('8_input.txt', 'r') as file:
    N, M, Q = [int(i) for i in file.readline().split()]

    A = file.readline().split()
    B = file.readline().split()

    result = ''

    for i in range(Q):
        change_type, player, card = file.readline().split()

        if change_type == '1':
            if player == 'A':
                A.append(card)
            else:
                B.append(card)
        else:
            if player == 'A':
                if card in A:
                    A.remove(card)
            else:
                if card in B:
                    B.remove(card)

        result += str(diversity(A, B)) + ' '

    print(result)
