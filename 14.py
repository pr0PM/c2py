## To print sum of odd and even terms 
## separately upto given terms

e=0
o=0
n = int(input("Enter the no of times u wanna loop : "))

for i in range(n+1):
    if i%2==0:
        e=i+e
    if i%2!=0:
        o=o+i
print('Sum of odd numbers')    
print(o)    
print('Sum of even numbers')
print(e)
