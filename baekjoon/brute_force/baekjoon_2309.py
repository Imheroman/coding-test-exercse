# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이
import sys
from itertools import permutations
from itertools import combinations

input = sys.stdin.readline

N = 9
TARGET_DWARF_NUMBER = 7
TARGET_HEIGHT = 100
dwarfs = [int(input()) for _ in range(N)]
# dwarfs = [20, 7, 23, 19, 10, 15, 25, 8, 13]

# for dwarf in permutations(dwarfs, TARGET_DWARF_NUMBER):
for dwarf in combinations(dwarfs, TARGET_DWARF_NUMBER):
    if sum(dwarf) == TARGET_HEIGHT:
        print(*sorted(dwarf), sep="\n")
        break
