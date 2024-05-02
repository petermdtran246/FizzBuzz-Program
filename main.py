target_number = int(input())
for n in range(1, target_number + 1):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)  # Only print the number if it's not divisible by 3 or 5
print()