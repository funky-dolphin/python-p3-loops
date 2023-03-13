#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    int_list=[1,2,3,4,5]
    squared_integers=[integer **2 for integer in int_list]
    return squared_integers

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
 