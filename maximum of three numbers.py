a=int(input('Enter the Number:'))
b=int(input('Enter the Number:'))
c=int(input('Enter the Number:'))
max = a
if b > max:
    max=b
elif c > max:
    max = c
else:
    print(max)
print('Maximum is:',max)