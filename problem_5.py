

num1 = y = 20
num2 = 1
while True:
    if num1%num2 == 0:
        num2 = num2 + 1
        if num2==y + 1:
            print('num1 = ',num1)
            exit()
        # print(num2)
    else:
        num1 = num1 + 1
        num2 = 1
