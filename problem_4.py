x = 0

for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        num = str(a*b)
        reverse = ''.join(reversed(num))

        if num == reverse:
            n = a*b
            if n > x:
                x = n
            break 
        
print('largest palindrome = ', x)