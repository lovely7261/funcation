# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)
 

# def function_multiply(a,b):
#     multiply=a*b
#     print(multiply) 
# function_multiply(5,7)


# def avg(number1,number2,number3):
#     avg=number1+number2+number3/3
#     print(avg)
# avg(1,3,2)
 

def voter(age):
    if age < 18:
        print("eligible")
    else:
        print("not eligible")
voter(20)

def distance(kms):
        if kms < 20:
            print("close")
        elif kms < 50:
            print("median")
        else:
            print("far")
distance(20)
