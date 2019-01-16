# Write a program that accepts the marks of 5 subjects and 
#find the sum and percentage obtained by the student.

print('________Marks Calculator_______')
print('Enter the max. marks possible in a subject:')
w = int(input())

print('Enter the marks of the following subjects:')
a = int(input('Maths:'))
b = int(input('English:'))
c = int(input('Physics:'))
d = int(input('Chemistry:'))
e = int(input('Computer Science:'))

# SUM
q = a+b+c+d+e
#PERCENT
p = q/(5*w)*100

print('_________')

print('Sum :' + str(q) + ' marks out of' + str(w*5) )
print('Percent : '+str(round(p,5))+' %')

#####################################
# To add funtionality 
# 1 Check the input to be under the max marks limit
# 2 Take the subjects to be input
# 3 Verify the sum and percentage to be under the maximum limit
# 4 ......
