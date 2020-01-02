def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0 and num % 5 !=0:
        return 'Fizz'
    elif num % 3 != 0 and num % 5 == 0:
            return 'Buzz'
    else:
        return num


for i in range(25):
    t = fizzbuzz(i)
    print(t)