size_of_pattern = int(input('Enter the size of the pattern: '))

row = 1

while row <= size_of_pattern:
    for column in range(size_of_pattern):
        print('*', end = "")
    print()
    row = row+1
