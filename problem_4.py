num1 = 999
num2 = 999
list = []

while num1 < 1000:
    while num2 < 1000:
        number = num1 * num2
        temp = str(number)
        reverse = int(''.join(reversed(temp))) #reversed elements and can join with join function
        if number == reverse :
            list.append(number)
            break
        else:
            num2 = num2 -1
    num1 = num1 - 1
    num2 = num2 -1



list=[]
list.append(99)
print(list)
list.append(89)
print(list)
print(max(list))