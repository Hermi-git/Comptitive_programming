# Problem: Runner-up Score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    unique_list = list(sorted(arr, reverse =True))
    print(unique_list[1])