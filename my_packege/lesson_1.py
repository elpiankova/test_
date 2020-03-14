import math
from sys import path
# help(math.acos)
#
# while True:
#     word = input("Enter number")
#     if word.isdigit():
#         break
#
# int(word)

def is_leap_year(year):
    return True

x = 10

def enter_number(times):
    # print(path)
    while True:
        i = input("Number:")
        try:
            i = float(i)
        except ValueError:
             print('not a number!!!!')
        else:
            break
    return i*times

# print(__name__)

if __name__ == "__main__":
    x +=1
    print("2:")
    print(enter_number(10))
