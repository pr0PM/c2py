# WAP to check weather an entred year is leap or not

# define a funtion to check the leapnesss...

def isleap(y):
    if y % 400 == 0 :
        return True
    elif y % 100 == 0 :
        return False
    elif y % 4 == 0:
        return True
    else: return False

# Execution part

y = int(input('Enter the year you want to check is leap :')) 
# Try to use try and exception here
#########
# funtion call and print  

print(isleap(y))


