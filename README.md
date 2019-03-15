print("enter a number")
num = int(input())

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
    
