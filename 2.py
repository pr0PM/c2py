# Write a program that prints simple interest and compound interest of the
# entered principal, time, rate, interest.
 
# Funtion for the SI
def si(p,r,t):
    print('The Simple Interest is ' + str(p*r*t/100))

# Funtion for the CI    
def ci(p,r,t):
    print('The Compound Inerest is ' + str())

# This is the main body 

print('-------------->>>>>>>>>>> Calculate SI and CI <<<<<<<<<<----------------')

print('Please enter the following data:')

p = int(input('Principal : '))
r = int(input('Rate : '))
t = int(input('Time : '))
    
print('________________')
print()
si(p,r,t)

print('________________')
print()
ci(p,r,t)
print()
print()
#########################################
# 1 Make functions
# 2 !!!!!Print out the interest only!!!!!!
# 3 ADDDD THE CI FORMULA   >>>>>>>>>>>>
#
#

