x = int(input("Escreva um valor: "))

y = int(input("Escreva outro valor: "))

operation = input ("Escolha uma operação (+, -, *, /): ")

if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    print(x/y)
else:
    print( "Você não indicou a operação matemática!")