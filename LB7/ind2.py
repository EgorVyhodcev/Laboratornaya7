#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    print("Enter the elements of the list a:")
    A = list(map(float, input().split()))
    length = len(A)
    print(length)
    print(f"The max element of this list is: {max(A)}")
    i = 0
    for index, el in enumerate(A):
        if el >= 0:
            i = index
    s = sum([a for index, a in enumerate(A) if index < i])
    print(f"The sum of numbers before the last positive element is: {s}")
    a = int(input("Enter the a number of the border:"))
    b = int(input("Enter the b number of the border:"))
    temp = [el for el in A if b < abs(el) or abs(el) < a]
    x = length - len(temp)
    temp.extend([0] * x)
    print(temp)
