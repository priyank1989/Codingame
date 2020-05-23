import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mime_type={}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_type[ext.lower()] = mt

print("Table", mime_type, file=sys.stderr)

for i in range(q):
    fname = input()  # One file name per line.
    extension = fname.split(".")[-1] if "." in fname else " "
    print(mime_type.get(extension.lower(), "UNKNOWN"))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
# print("UNKNOWN")
