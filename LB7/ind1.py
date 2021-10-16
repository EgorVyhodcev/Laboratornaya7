#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    s = sum([a for a in A if 3 < a < 8])
    print(f"The sum of numbers more than 3 and less than 8 is: {s}")
