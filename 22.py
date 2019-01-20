# Write a program that takes 2 arrays as input and prints the sum of the corresponding elements 
# in the third arrays

print('Enter the first array : ')

a = [int(x) for x in input().split()]

print('Enter the second array : ')

b = [int(x) for x in input().split()]

print('The sum of corresponding elements of the entered arrays is : ')

c = []

for i in range(len(a)):
    c.append(a[i] + b[i])  
    
print('The sum is : ',c)








