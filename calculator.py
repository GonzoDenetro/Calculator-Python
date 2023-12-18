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
    #Recibimos la operación en partes en forma de lista, vamos a unir los números.
    print(f'2..- {operation_list}') 

    operadores = ['+', '-', '/', '*']
    num = [] #En el array vamos a tener el número por partes
    elem_operacion = [] #En esta lista guarademos todos los elementos de la operación
    
    for elem in operation_list: #Recorremos el array donde esta la operación
        if elem not in operadores: 
            #Si el elemento que tenemos no es un operador lo agregarmos a la lista.
           num.append(elem)
           print(num)
        else:
            #Cuando el elemento sea el operador, es que ya tenemos el primer número completo, y el operador.
            #Repetimos para obtener el siguiente número
            operador = elem 
            num1 = int("".join(num)) # join() lo que hace es los elementos de una lista pasarlos a string
            elem_operacion.append(num1)
            elem_operacion.append(operador)
            print(num1, operador)
            num = []
    num2 = int("".join(num))
    elem_operacion.append(num2)
    print(elem_operacion)
    return elem_operacion
    
    #return num1, operador, num2

def calculator(operacion):
    operation_por_partes = deleteSpaces(operacion)
    operacion_elem = joinNums(operation_por_partes)
    operadores = ['+', '-', '/', '*']
    result = 0
    
    while len(operacion_elem) > 1:
        #Hacemos la operación, el resultado lo agregamos a la lista, y eliminamos los elementos que ya usamos.
        #Hasta que en la lista solo quede el un elemento que es el resultado
        print("----",operacion_elem)
        num1 = operacion_elem[0]
        operator = operacion_elem[1]
        num2 = operacion_elem[2]    
    
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
        
        print(result)
        print(operacion_elem)
        operacion_elem.insert(0, result)
        print(operacion_elem)
        operacion_elem.remove(num1)
        print(operacion_elem)
        operacion_elem.remove(operator)
        print(operacion_elem)
        operacion_elem.remove(num2)
        print(operacion_elem)
            
    return result


def run():
    print("CALCULADORA")
    operacion = input("Introduce tu operación: ")
    result = calculator(operacion)   
    print(f'Tu resultado es {result}')


if __name__ == '__main__':
    run()
    