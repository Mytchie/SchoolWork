def main():
    while True:
        try:
            number = int(input("Enter a 3-digit such with digits in order: "))
            s = str(number)
            valid = len(s) == 3
            for i in range(1, len(s)):
                if s[i] < s[i-1]:
                    valid = False
            if valid:
                break
        except:
            pass
        print("Invalid number. Try again!")
    print("Valid number = " + str(number))