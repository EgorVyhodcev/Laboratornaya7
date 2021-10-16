#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("Enter the elements of the list a:")
    A = list(map(float, input().split()))
    length = len(A)
    print(length)
    print(f"The max element of this list is: {max(A)}")
    i = 0
    for el in A:
        if el >= 0:
            i = A.index(el)
    s = sum([a for a in A if A.index(a) < i])
    print(f"The sum of numbers before the last positive element is: {s}")
    a = int(input("Enter the a number of the border:"))
    b = int(input("Enter the b number of the border:"))
    for el in A:
        if a < abs(el) < b:
            A.pop(A.index(el))
    print(len(A))
    if length > len(A):
        for i in range(length - len(A)):
            A.append(0)
    print(A)
