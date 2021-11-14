# printing Simple addition caliculater using input and eval 
a=4
b=9
result=a+b
print(result)
# 	or 
print(f"The Addition of 'a' and 'b' is : {result}")

#	Note: Hear we are fixing the a nd b value  so ther is no chaing result 

# Read the Input from command line every time 

a=input("enter the 'a' value : ")
b=input("enter the 'b' value : ")

print(f"The Value of 'a' is {a} The type of 'a' is : {type(a)}")


# hear converting to integer

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))

print(f"The Value of 'a' is {a} The {type(a)}")


# hear converting to integer using eval function

a=eval(input("Enter the value of a : "))
b=eval(input("Enter the value of b : "))
print(f"The Value of a is : {a} the type is :{type(a)}")