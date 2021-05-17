# def calculater(num_x ,num_y):
#     num1=int(input("enter the number"))
#     num2=int(input("enter the number"))
#     sum= (num_x + num_y)
#     if sum=="+":
#         return(num_x +num_y,"add")
#     elif sum=="-":
#         return(num_x -num_y,"min")
#     elif sum=="*":
#         return(num_x *num_y,"multiply")
#     elif sum=="%":
#         return(num_x % num_y,"divd")
#     else:
#         return("nonthing")
# calculater(5,8)    
    
def calculater(x,y):
    return(x,y)
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divid")
choice = input ("enter choice(1/2/3/4):")
num1 =int(input("enter the 1st number"))
num2 =int(input("enter the 2nd number"))
if choice=="1":
    print(num1,"+",num2,"=","add",(num1+num2))
elif choice=="2":
    print(num1,"-",num2,"=","subtract",(num1-num2))
elif choice=="3":
    print(num1,"*",num2,"=","multiply",(num1*num2))
elif choice=="4":
    print(num1,"%",num2,"=","divid",(num1%num2))
else:
    print("invelid number")

