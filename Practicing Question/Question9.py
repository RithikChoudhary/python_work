# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    sm = ""
    listing = list(s)
    for i in listing:
        if(i.isupper()):
            sm = sm + str(i.lower())
        elif(i.islower()):
            sm = sm + str(i.upper())
        else:
            sm = sm + i
    return sm

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    