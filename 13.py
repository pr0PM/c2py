# factorial of a number.'

# Take input once and print the results from the same input 

import math as m
n = int(input("Factorial : "))
print(m.factorial(n))

print('_________________')
# Again without using built in function
p = 1
for i in range(1,n+1):
    p = p * i
print(p)
