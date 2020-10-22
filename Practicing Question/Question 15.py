# Input Format

# The first line contains an integer,
# , denoting the number of commands.
# Each line of the

# subsequent lines contains one of the commands described above.

# Constraints

#     The elements added to the list must be integers.

# Output Format

# For each command of type print, print the list on a new line.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]



if __name__ == '__main__':
    N = int(input())
    diction = {}
    fin = []
    for _ in range(N):
        first, *line = map(input()).split()
        listing = list(map(int, line))
        diction[first] = listing
        for key, value in diction.items():
            if key == 'insert':
                fin.insert(value[0], value[1])
            if key == 'print':
                print(fin)
            if key == 'remove':
                fin.remove(value[0])
            if key == 'append':
                fin.append(value[0])
            if key == 'sort':
                fin.sort()
            if key == 'pop':
                fin.pop()
            if key == 'reverse':
                fin.reverse()
