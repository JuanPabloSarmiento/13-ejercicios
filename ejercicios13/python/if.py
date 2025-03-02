#fases de grupos
cuartos = []
semis = []
finales = []
octavos =  [
    "Países Bajos",
    "Estados Unidos",
    "Argentina",
    "Australia", 
    "Francia",
    "Polonia",
    "Inglaterra",
    "Senegal",
    "Japón",
    "Croacia",
    "Brasil",
    "Corea del Sur",
    "Marruecos",
    "España",
    "Portugal",
    "Suiza",
]

#mostrar los equipos de octavos
print(f"equipos en octavos de final {octavos}")

#funcion de enfrentamientos para clasificar a los ganadores
def enfrentamientos(pais1,goles1,pais2,goles2,fase):
    if goles1 > goles2:
        fase.append(pais1)
        return print(f"el resultado es {pais1} = {goles1} - {goles2} = {pais2} \n -----{pais1} avanza a la siguiente ronda ------ ") 
    else:
        fase.append(pais2)
        return print(f"el resultado es {pais1} = {goles1} - {goles2} = {pais2} \n -----{pais2} avanza a la siguiente ronda ------ ") 

#los bucles while son usados para repetir seccion en caso de que haya un error
faseEnfrentamiento = cuartos   #se nombra la fase posterior para guardar en el parametro de la funcion y asi usar el append para clasificar 
#el try y except es para repetir el enfrentamiento si se ingresan tipos de datos incorrectos
for i in range(0,16,2):
    contador = 0;
    while contador < 1:
        try:
            print(f"el enfrentamiento es {octavos[i]} vs {octavos[i+1]}")
            paisn1= octavos[i]
            golesn1 = int(input(f"digite los goles del pais {octavos[i]} "))
            paisn2= octavos[i+1]
            golesn2 = int(input(f"digite los goles del pais {octavos[i+1]} "))

            if (paisn1 in octavos and paisn2 in octavos and golesn1 != golesn2):
                    enfrentamientos(paisn1,golesn1,paisn2,golesn2,faseEnfrentamiento);
                    break
            else:
                    print(f"nombre de equipo o invalido o resultado incorrecto")
        except ValueError : print("datos incorrectos, digite de nuevo")
            
#imprime los equipos de cuartos
print(f"los paises clasificados son {cuartos}")
faseEnfrentamiento = semis

for i in range(0,8,2):
    contador = 0;
    while contador < 1:
        try:
            print(f"el enfrentamiento es {cuartos[i]} vs {cuartos[i+1]}")
            paisn1= cuartos[i]
            golesn1 = int(input(f"digite los goles del pais n1: {cuartos[i]} "))
            paisn2= cuartos[i+1]
            golesn2 = int(input(f"digite los goles del pais {cuartos[i+1]} "))
            if (paisn1 in octavos and paisn2 in octavos and golesn1 != golesn2):
                enfrentamientos(paisn1,golesn1,paisn2,golesn2,faseEnfrentamiento);
                break
            else:
                print(f"nombre de equipo o invalido o resultado incorrecto")
        except ValueError : print("datos incorrectos, digite de nuevo")
           
     
#imprime los equipos de semis 
print(f"los paises clasificados son {semis}")
faseEnfrentamiento = finales

for i in range(0,4,2):
    contador = 0;
    while contador < 1:
        try:
            print(f"el enfrentamiento es {semis[i]} vs {semis[i+1]}")
            paisn1= semis[i]
            golesn1 = int(input(f"digite los goles del pais n1: {semis[i]} "))
            paisn2= semis[i+1]
            golesn2 = int(input(f"digite los goles del pais {semis3[i+1]} "))
            if (paisn1 in octavos and paisn2 in octavos and golesn1 != golesn2):
                enfrentamientos(paisn1,golesn1,paisn2,golesn2,faseEnfrentamiento);
                break
            else:
                print(f"nombre de equipo o invalido o resultado incorrecto")
        except ValueError : print("datos incorrectos, digite de nuevo")
     

print(f"los paises clasificados son {finales}")
faseEnfrentamiento = "";

for i in range(1):
    contador = 0;
    while contador < 1:
        try:
            golesn1 = int(input(f"digite los goles del pais n1: {semis[i]} "))
            golesn2 = int(input(f"digite los goles del pais {semis3[i+1]} "))
            if(paisn1 in finales and paisn2 in finales and golesn1 != goles2):
                enfrentamientos(finales[0],golesn1,finales[1],golesn2,faseEnfrentamiento);
                break
            else: print(f"equipo de nombre invalido o resultado incorrecto")
        except ValueError : print("datos incorrectos, digite de nuevo")
 
print(f"el ganador es {faseEnfrentamiento}")