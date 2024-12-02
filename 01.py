from collections import Counter

from utils import *
def ex_01_0():
    A, B = [], []
    with open('test/01_0.txt') as f:
        for line in f.readlines():
            a, b = line.split('   ')
            A.append(int(a))
            B.append(int(b))
    A = sorted(A)
    B = sorted(B)
    abs_diff = 0
    for a,b in zip(A,B):
        abs_diff += abs(a-b)
    return abs_diff

def ex_01_1():
    A, B = Counter(), Counter()
    with open('test/01_1.txt') as f:
        for line in f.readlines():
            a, b = line.split('   ')
            A[int(a)] +=1
            B[int(b)] +=1
    diff = 0
    for key in A:
        if key in B:
            diff += key * B[key]
    return diff

print(ex_01_0())
print(ex_01_1())
