# lists in Python are implemented as dynamic arrays of references
marks = [2, 2, 3, 4]
marks[0] = 3  # O(1)

lst = [True, 'True', 1, 1.0, 5]
lst.append(6)  # O(1)
lst.insert(0, 'First')  # O(n)

n = len(marks)
m = len(marks)
marks_plus_lst = marks + lst  # O(n+m)

lst_1 = [1, 2, 3, 4, 5]
lst_2 = lst_1[1:4]  # O(n)


