def add(a, b):
    print(a+b)
def sub(a, b):
    print(a - b)
def mult(a, b):
    print(a * b)
def div(a, b):
    print(a / b)

a = int(input("Enter first oprand: "))
b = int(input("Enter second oparand: "))

m = input("Enter your operation +, -, /, *  : ")

if m == '+':
    add(a, b)
elif m == '-':
    sub(a, b)
elif m == '*':
    mult(a, b)
elif m == '/':
    div(a, b)