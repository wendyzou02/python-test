def sum_even(start_num, end_num):
    sum = 0
    for x in range( start_num, end_num+1 ):
        if x%2==0:
            sum += x
    return sum


