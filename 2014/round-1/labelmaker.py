#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_label_length_and_num(L, N):
    length, summary = 0, 0

    for i in range(1, 51):
        prev_sum = summary
        summary += len(L) ** i
        length = i
        if (summary >= N):
            break

    return length, (N - prev_sum)

def solve():
    L, N = input().split(' ')
    N = int(N)
    label_length, n = get_label_length_and_num(L, N)
    last_n = n
    ans = list(L[0] * label_length)
    mod = n % len(L)

    ans[0] = L[mod-1] if mod else L[-1]

    if label_length < 2:
        return ''.join(reversed(ans))

    for i in range(label_length-1, 0, -1):
        for j in range(1, len(L)+1):
            if (len(L) ** i) * j < last_n:
                continue
            ans[i] = L[j-1]
            break
        last_n -= (len(L) ** i) * (j - 1)

    return ''.join(reversed(ans))

def main():
    T = int(input())
    for i in range(T):
        print('Case #{i}: {answer}'.format(i=i+1, answer=solve()))

if __name__ == '__main__':
    main()
