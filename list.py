data_tuple = ('u', 'o', 6.13, True, 'y', '1', 'e', 'r', 'a', ' ',
              'w', 'o', 'h', ' 3', 'e', 'n', 'o', ' ', 'y', 'n',
              'a', ' ', 'o', 'l', 'l', 'e', 'h')

letters = []
numbers = []

for item in data_tuple:
    if type(item) == str:
        letters.append(item)
    else:
        numbers.append(item)

numbers.remove(6.13)

numbers.remove(True)
letters.append(True)

index_3 = letters.index(' 3')
letters.insert(index_3 + 1, 2)

numbers.sort()

letters.reverse()

letters[0] = 'H'
letters[1] = 'E'

print("Letters:", letters)
print("Numbers:", numbers)
