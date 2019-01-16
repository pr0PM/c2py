# Write a program to comvert tne temprature from 
# Celcius to Fahrenheite or vice versa

# The funtions are made for practice XD 

def c2f(b):
    f = 9/5*b + 32
    print('Fahrenheite : ' + str(f))

def f2c(a):
    c = 5/9(a-32)
    print('Celcius : ' + str(c))


# The program begins here!!!!!!!!!!

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^Celcius to Fahrenheite or Fahrenheite to Celcius^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

print('Choose the type of converson you want:')

print('1.Celcius to Fahrenheite')

print('2.Fahrenheite to Celcius')

print('3.Exit')

while True :
    p = input('Enter your Choice :')

    if p=='1':
        print('Celcius to Fahrenheite')
        c = int(input('Celcius : '))
        c2f(c)

    elif p=='2':
        print('Fahrenheite to Celcius')
        f = int(input('Fahrenheite : '))
        f2c(f)
    
    elif p=='3': break   ###### To Exit
    
    else:
        print('Wrong Input. Try Again!! ')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    continue


###################################################
# 1. ........?????
#
#
#
#
#
