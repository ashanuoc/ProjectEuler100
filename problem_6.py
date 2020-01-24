
def sum_sqr_diff(num):

    sqr_sum = 0
    for a in range(1,num+1,1):
        sqr_sum = sqr_sum + a*a
    
    sum_sqr = sum(list(range(1,num+1,1)))**2

    return sum_sqr - sqr_sum


print(sum_sqr_diff(100))