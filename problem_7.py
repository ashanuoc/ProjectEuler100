def prime_num(num):
    for a in range(2,num,1):
        if num%a ==0:
            return False
            
            
    return True
    



i = 1
num = 3
while i < 10002:
    if prime_num(num):
        i =  i+1
    
    
    if i == 10001:
        print('1001st prime = ', num)
        break
    
    num=num+1

