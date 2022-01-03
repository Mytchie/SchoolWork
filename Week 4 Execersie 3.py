    # get user input and convert to int using int()

    n = int(input('Enter a number : '))

    # if n is in range [2 , 20] and divisible by 3

    if n >= 2 and n <= 20 and int(n % 3) == 0:

        print('%d is in range [2 , 20] and divisible by 3' % (n))



    else:

        print('%d is NOT in range [2 , 20] and divisible by 3' % (n))