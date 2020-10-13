# In Python, a string can be split on a delimiter. 


def split_and_join(line):
    # write your code here
    spliting = line.split(" ")
    spliting = "-".join(spliting)
    return spliting

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)