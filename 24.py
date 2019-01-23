# This is a program to implement the linear search technique in the 
# given array to search an element.

# First we will take an  array as input from the user

print('Enter the Array with any no of elements and spaces in between the consecutive elements: ')

l = [x for x in input().split()]

# Enter the element to be searched for 
n = input('Enter the search : ')

# implement the search 
# using for loop 
'''
for i in l:
    if i==n:
        p = True
    else:p = False

if p==True :
    print('element present in the entered list !')
else : print('NO such element exists!!!!')
'''

for i in range(len(l)):
    if l[i] == n:
        print('Element found at position : '+ str(i+1))
   # else : print('404 not found')
