def check_numbers_list(a,b):
    i=0
    sum=0
    while i<b:
        if i%3==0 or i%5==0:
            sum=sum+1
            return(i)
        i=i=1
    return("sum is",sum)
a=check_numbers_list(0,6)
print(check_numbers_list)
check_numbers_list()

