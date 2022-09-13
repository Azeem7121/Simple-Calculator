""" SIMPLE CALCULATOR"""
print("""SIMPLE CALCULATOR
- (Subtraction)
+ (Addition)
* (Multiplication)
/ (Division)
""")
num1 = int(input("Enter first number: "))
opr = input("Enter operation (- + * /): ")
num2 = int(input("Enter second number: "))
if opr == "-":
    print(num1-num2)
elif opr == "+":
    print(num1+num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else:
    print("Please Enter Valid Operation")
