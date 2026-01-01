def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b == 0:
        print("Can't divide by zero...")
        return
    return a / b

operations = {
    '+': add,
    '-':sub,
    '*': mult,
    '/': div
}

while True:
    try:
        a = int(input("Enter first oprand: "))
        b = int(input("Enter second oparand: "))
    except ValueError:
        print("Please Enter a valid integer")
        continue

    m = input("Enter your operation +, -, /, *  : ")
    if m not in operations:
        print("Enter a valid operation...")
        continue
    result = operations[m](a,b)
    print(result)
    sign = input("Enter q to quit or c to continue: ")
    if sign == 'q':
        break