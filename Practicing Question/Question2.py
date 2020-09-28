if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ab=sorted(set(arr))
    lenn=len(ab)
    print(ab[-2])