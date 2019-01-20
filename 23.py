# Program to find the max and min elements of the array

# Take an array as input
print('Enter all the element of your array using spaces between each elements (integes only) : ',end="\n")

l = [int(x) for x in input().split()]

print('The max element is : ',max(l))
print('The min element is : ',min(l))
