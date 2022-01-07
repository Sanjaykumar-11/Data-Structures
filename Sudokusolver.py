class Slot:
    r = 0
    c = 0

def solve(matrix):
    slot = Slot(getFreeSlot(matrix))


matrix = []

slot = Slot()

for i in range(9):
    l = list(map(int, input().split()))
    matrix.append(l)

if solve(matrix):
    for i in range(9):
        for j in range(9):
            print(matrix[i][j], end=" ")
        print()
else:
    print("Not Solved!")