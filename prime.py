# -*- coding: utf-8 -*-
"""
objective: To Check the given number is Prime or not

Description: Analysing the number is Prime or not by dividing the number by all
the given numbers from 2 to the (given number-1). If the remainder becomes zero
then it is considered as Prime Number

Created on Thu Mar 14 00:33:00 2019

@author: (sachinbandc)- Sachin Channaiah

Test Cases: 1.If the given number is less than zero--->>Not a prime number
            2. If the given number is greater than zero and the remainder is
            not zero---->>>>Not a prime number
            3.If the given number is greater than zero and the remainder is
            zero---->>>>It is a prime number

Initial Static code Analysis---->>>> -5/10
Final Static code Analysis------>>>> 8/10

"""


num = 765

if num > 1:
    for i in range(2, num):
        a=(num % i)
    if a==0:
        print(num, "is not a prime number")
        print(i, "times", int(num/i), "is", num)
    else:
        print(num, "is a prime number")



else:
    print(num, "is not a prime number")
