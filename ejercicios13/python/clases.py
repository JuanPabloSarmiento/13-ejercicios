lista1 = [1,2,3,4,5];
lista2 = [3,4,5,6,7];
lista3 = []

def operaciones():
    operador = input(f"que operacion desea realizar:\n------ \n --------\n 1. suma \n 2. resta \n 3.multiplicacion \n 4. division \n ------ \n --------\n ")
    match operador:
        case "1":
            for i in range(len(lista1)):
                lista3.append(lista1[i] + lista2[i]) 
            return print(f"{lista3}")
        case "2":
            for i in range(len(lista1)):
                lista3.append(lista1[i] - lista2[i]) 
            return print(f"{lista3}")
        case "3":
            for i in range(len(lista1)):
                lista3.append(lista1[i] * lista2[i]) 
            return print(f"{lista3}")
        case "4":
            if num2==0:
                return "error: no se puede dividir por 0"
            else:
                for i in range(len(lista1)):
                    lista3.append(lista1[i] / lista2[i]) 
            return print(f"{lista3}")
        case _:
             "Operador invalido"



operaciones()

