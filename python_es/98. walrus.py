# walrus = False
# print(walrus)
print(walrus := True)
print(type(walrus))


# rows = input('Enter the number of rows: ')
# for i in range(int(rows)):
#     print('*'*(i+1))

for i in range(int(rows := int(input('Enter the number of rows: ')))):
    print('*'*(i+1))


def read_file(fp):
    while True:
        line = fp.readline()
        if not line:
            break
        split_line = line.split()
        print(split_line[1])


def read_file_2(fp):
    while line := fp.readline():
        if not line:
            break
        split_line = line.split()
        print(split_line[1])