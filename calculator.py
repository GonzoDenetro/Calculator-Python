def deleteSpaces(operacion):
    list_operation = list(operacion) #Pasamos nuestro string a una lista
    print(f' 1.-  {list_operation}')
    elementos_operacion = []
    for element in list_operation:
        if element.find(' ') == -1:
            #Lo que hace find() es buscar un espacio, si no lo encuentra regresa -1
             elementos_operacion.append(element)
    return elementos_operacion

def joinNums(operation_list):
    print(f'2..- {operation_list}')

    operadores = ['+', '-', '/', '*']
    num = [] #En el array vamos a tener el número por partes
    
    for elem in operation_list: #Recorremos el array donde esta la operación
        if elem not in operadores: 
            #Si el elemento que tenemos no es un operador lo agregarmos a la lista.
           num.append(elem)
           print(num)
        else:
            #Cuando el elemento sea el operador, es que ya tenemos el primer número completo, y el operador.
            #Repetimos para obtener el siguiente número
            operador = elem 
            num1 = "".join(num) # join() lo que hace es los elementos de una lista pasarlos a string
            print(num1, operador)
            num = []
    num2 = "".join(num)
    print(num1, operador, num2)
    
    return num1, operador, num2

def calculator(operacion):
    elem_operation = deleteSpaces(operacion)
    num1, operator, num2 = joinNums(elem_operation)
    num1 = int(num1)
    num2 = int(num2)
    
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
    result = calculator(operacion)   
    print(f'Tu resultado es {result}')


if __name__ == '__main__':
    run()
    