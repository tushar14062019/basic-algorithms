num = int(input('Enter the Number: '))

if num < 2:
    print('give correct input')
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print('not prime')
            break
    else:
        print('is prime')
