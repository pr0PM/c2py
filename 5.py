# Write a program that swaps the value of two variables using 
# a third variable.

p = ''
# The Function

def swap(q,w):
    p = q
    q = w
    w = p
    print('WHOOOOOOSHHHH....Vars Swapped')
    print('A = ' + q)            # Final Output
    print('B = ' + w)

# The main body begins

print('Swap the variables : ')

a = input('Enter the value of A = ')
b = input('Enter the value of B = ')

swap(a,b)           # Funtion Call

