a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
op = input("Podaj operator: ")
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*" or op == "x":
    print(a*b)
elif op == "/" and b != 0:
    print(a/b)