import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())

ASCII_char={
    "A" : 0,
    "a" : 0,
    "B" : 1,
    "b" : 1,
    "C" : 2,
    "c" : 2,
    "D" : 3,
    "d" : 3,
    "E" : 4,
    "e" : 4,
    "F" : 5,
    "f" : 5,
    "G" : 6,
    "g" : 6,
    "H" : 7,
    "h" : 7,
    "I" : 8,
    "i" : 8,
    "J" : 9,
    "j" : 9,
    "K" : 10,
    "k" : 10,
    "L" : 11,
    "l" : 11,
    "M" : 12,
    "m" : 12,
    "N" : 13,
    "n" : 13,
    "O" : 14,
    "o" : 14,
    "P" : 15,
    "p" : 15,
    "Q" : 16,
    "q" : 16,
    "R" : 17,
    "r" : 17,
    "S" : 18,
    "s" : 18,
    "T" : 19,
    "t" : 19,
    "U" : 20,
    "u" : 20,
    "V" : 21,
    "v" : 21,
    "W" : 22,
    "w" : 22,
    "X" : 23,
    "x" : 23,
    "Y" : 24,
    "y" : 24,
    "Z" : 25,
    "z" : 25,
}

ASCII_input=[]
t = input()
print("Debug messages...",l, h, t, file=sys.stderr)
for i in range(h):
    row = input()
    ASCII_input.append(row)        

for j in range(h):
    for char in t:
        char_position=ASCII_char.get(char, 26)
        for i in range(len(ASCII_input[0])):
            if char_position*l <= i < (char_position+1)*l:
                print(ASCII_input[j][i], end="")
    print()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
#
#print("answer")
