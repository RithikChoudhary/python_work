if __name__ == '__main__':
    n = int(input())
    # here we fetch the value and split it by space and append in integer_list by map
    integer_list = map(int, input().split())
    # here we convert the integer_list into tuple 
    tup = tuple(integer_list)
    print(hash(tup))
