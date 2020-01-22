num1 = 99
num2 = 99


while num2 < 100:
    number = num1 * num2
    temp = str(number)
    reverse = int(''.join(reversed(temp))) #reversed elements and can join with join function
    if number == reverse :
        print('largest palindrome = ', number)
        break
    else:
        num2 = num2 -1

