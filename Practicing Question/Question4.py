if __name__ == '__main__':

    studentTotal = {}
    n = int(input())
    
    

    for _ in range(n):
        # name get the first input and rest input will be stored in line
        name, *line = input().split()
        marks = list(map(float, line))
        # it is a dictionary save the list and name
        studentTotal[name] = marks
    query_name = input()
    score = 0
    if studentTotal.get(query_name):
        for i in studentTotal.get(query_name):
            score = i+score
        show = score/3
        # it is use to get 2 deciaml place value by using format
        print("{0:.2f}".format(show))

