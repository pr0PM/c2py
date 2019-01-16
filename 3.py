# Write a program to calculate the 
# area and the circumference of the circle

print('>>>>>>>>>>>>>Calculate the AREA and CIRCUMFERENCE<<<<<<<<<<<<<<<')

print('Choose The Input Method: ')
print('1.Radius')
print('2.Diameter')
print('3.Exit')

while True :
    n = int(input('Enter your choice : '))
    
    if(n==1):
        i = int(input("Enter the Radius ")) 
        r = i
        break
    
    elif(n==2):
        i = int(input("Enter the Diameter "))
        r = i/2
        break
    
    elif(n==3):break
    
    else:
        print('!!!Wrong input Try Again!!! ')

# Area
print('Area of the circle:' + str(round(3.14*pow(r,2))))

# Circumference
print('Circumference of Circle:' + str(round(3.14*2*r)))

##########################################################
# 1 Check input at every stage of input for nums.....
#
#
