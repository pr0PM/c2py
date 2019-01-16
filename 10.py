# This part copied from the 1.py to enter marks
# of the student

print('________Marks Calculator_______')
print('Enter the max. marks possible in a subject:')
w = int(input())

print('Enter the marks of the following subjects rounding off to the nearest integer:')
a = int(input('Maths:'))
b = int(input('English:'))
c = int(input('Physics:'))
d = int(input('Chemistry:'))
e = int(input('Computer Science:'))

# SUM
q = a+b+c+d+e
#PERCENT
p = q/(5*w)*100
p1 = round(p,5)
print('_________')
print('Percent : '+str(p1)+' %')

# To print grade according to the percentage
# obtained by the student

if p1 > 90:
    print("Grade : A")
elif p1 > 80:
    print("Grade : B")
elif p1 > 60:
    print("Grade : C")
else : 
    print("Grade : D")
    
