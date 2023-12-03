def calculator(num1, num2, operator):        
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*' or operator == 'x':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("No tenemos esa operación disponible")
    return result


def run():
    print("CALCULADORA")
    operacion = input("Introduce tu operación: ")
    user_num1 = int(input("Introduce tu primer número: "))
    user_num2 = int(input("Introduce tu segundo número: "))
    operador = input("Introduce el operador de tu operación (+, -, *, /)" )
    result = calculator(user_num1, user_num2, operador)
    print(f'Tu resultado es {result}')


if __name__ == '__main__':
    run()
    