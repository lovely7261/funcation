def check_numbers_list ():
    list1=[2,4,6,8,10,]
    list2=[12,14,16,18,20]
    i=0
    while i<len(list1):
        if list1[i]%2==0:
            if list2[i]%2==0:
                print("even number")
        print("not even numbers")
        i=i+1   
check_numbers_list ()