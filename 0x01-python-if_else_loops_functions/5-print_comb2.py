#!/usr/bin/python3

val = 0
while val <= 99:
    if val < 10 and val != 99:
        print(f"0{val}", end=", ")
    elif val > 9 and val != 99:
        print(f"{val}", end = ", ")
    else:
        print(f"{val}")
    val += 1
