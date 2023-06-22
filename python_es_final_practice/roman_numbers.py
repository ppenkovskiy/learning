romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


def parse_roman(roman):
    result = 0
    for i, c in enumerate(roman):
        if i+1 < len(roman) and romans[roman[i]] < romans[roman[i+1]]:
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]
    return result


print(parse_roman('I') == 1)
print(parse_roman('II') == 2)
print(parse_roman('IV') == 4)
print(parse_roman('VI') == 6)
print(parse_roman('VII') == 7)
print(parse_roman('V') == 5)
print(parse_roman('IX') == 9)
print(parse_roman('LC') == 50)