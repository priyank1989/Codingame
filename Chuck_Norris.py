import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
binary_message = ""
for char in message:
    binary_value = bin(ord(char))[2:]
    binary_message += binary_value.zfill(7)

print("Message", binary_message, file=sys.stderr)


count=1
chuck_norris_message=""
if len(binary_message) > 1:
    for i in range(1, len(binary_message)):
       if binary_message[i-1] == binary_message[i]:
          count += 1
       else :
           chuck_norris_message += ("00" if binary_message[i-1] == "0" else "0" ) + " " + str("0" * count) + " "
           count=1
    chuck_norris_message += (("00" if binary_message[i] == "0" else "0" ) + " " + str("0" * count)) + " "
else:
    i=0
    chuck_norris_message += (("00" if binary_message[i] == "0" else "0" ) + " " + str("0" * count))

print(chuck_norris_message[:-1])   

