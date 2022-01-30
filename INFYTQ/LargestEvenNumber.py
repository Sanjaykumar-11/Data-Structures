S = input().strip()
numbers = []
for i in S:
    if i.isnumeric() and i not in numbers:
        numbers.append(i)

for index, number in enumerate(numbers):
    temp = numbers
    temp.remove(number)

