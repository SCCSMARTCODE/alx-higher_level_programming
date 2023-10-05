#!/usr/bin/python3
import calculator_1 as cal

a = 10
b = 5

add_val = cal.add(a, b)
sub_val = cal.sub(a, b)
mul_val = cal.mul(a, b)
div_val = cal.div(a, b)

print("{} + {} = {}".format(a, b, add_val))
print("{} - {} = {}".format(a, b, sub_val))
print("{} * {} = {}".format(a, b, mul_val))
print("{} / {} = {}".format(a, b, div_val))

