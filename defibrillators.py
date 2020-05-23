import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def fix_lon_lat_values(value):
    return float(value.replace(",", "."))

lon = fix_lon_lat_values(input())
lat = fix_lon_lat_values(input())

n = int(input())

closest_defib=[]
closest_distance=0

def get_distance(defib):
    given_defib = defib
    given_defib_lat = fix_lon_lat_values(given_defib[-1])
    given_defib_lon = fix_lon_lat_values(given_defib[-2])
    x_axis = (given_defib_lon - lon) * math.cos((given_defib_lat + lat) / 2)
    y_axis = (given_defib_lat - lat)
    distance = math.sqrt( math.pow(x_axis, 2) + math.pow(y_axis, 2)) * 6371
    return distance

for i in range(n):
    defib = input().split(";")
    if i == 0:
        closest_defib = defib
        closest_distance = get_distance(closest_defib)
        continue
    defib_distance = get_distance(defib)
    if closest_distance > defib_distance:
        closest_defib = defib
        closest_distance = defib_distance

print(closest_defib[1])
    



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

