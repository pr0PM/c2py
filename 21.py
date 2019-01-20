# Take an array (list) of elements as input and print the sum of all
# the entered numbers

n = int(input('Enter the total number of elements you want : '))
a = 0

print('Enter the nos : ')

l = [int(x) for x in input().split()]

print('________------________')

for i in l:
    a = a + int(i)

print()# To change the line

print('The sum is :',a)
