#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    L, N = input().split(' ')
    N = int(N)
    result = ''

    while N > 0:
        N -= 1
        result = L[N % len(L)] + result
        N = int(N / len(L))

    return result

def main():
    T = int(input())
    for i in range(T):
        print('Case #{i}: {answer}'.format(i=i+1, answer=solve()))

if __name__ == '__main__':
    main()
