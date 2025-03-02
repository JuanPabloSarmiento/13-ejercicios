

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
for equipos in octavos:
    equipos.lower()

print(f"equipos en octavos de final {octavos}")


def enfrentamientos(pais1,goles1,pais2,goles2,fase):
    if goles1 > goles2:
        return fase.append(pais1)
        print(f"el resultado es {pais1} = {goles1} - {goles2} = {pais2} \n -----{pais1} avanza a la siguiente ronda ------ ") 
    else:
        print(f"el resultado es {pais1} = {goles1} - {goles2} = {pais2} \n -----{pais1} avanza a la siguiente ronda ------ ")
        return fase.append(pais2) 
         


faseEnfrentamiento = cuartos
for i in range(8):
    paisn1= (input("digite el pais n1: ")).lower()
    golesn1 = int(input("digite los goles del pais n1: "))
    paisn2= (input("digite el pais n2: ")).lower()
    golesn2 = int(input("digite los goles del pais n2: "))
    if(paisn1 in octavos and paisn2 in octavos and goles1 == goles2):
        enfrentamientos(paisn1,golesn1,paisn2,golesn2,faseEnfrentamiento);
    else: i = i - 1
    print(f"equipo de nombre invalido o resultado incorrecto")

print(f"los paises clasificados son {cuartos}")
faseEnfrentamiento = semis

for i in range(4):
    paisn1= str(input("digite el pais n1: ")).lower()
    golesn1 = int(input("digite los goles del pais n1: "))
    paisn2= str(input("digite el pais n2: ")).lower()
    golesn2 = int(input("digite los goles del pais n2: "))
    if(paisn1 in cuartos and paisn2 in cuartos and goles1 == goles2):
        enfrentamientos(paisn1,golesn1,paisn2,golesn2,faseEnfrentamiento);
    else: i = i - 1
    print(f"equipo de nombre invalido o resultado incorrecto")
     

print(f"los paises clasificados son {semis}")
faseEnfrentamiento = finales

for i in range(2):
    paisn1= str(input("digite el pais n1: ")).lower() 
    golesn1 = int(input("digite los goles del pais n1: "))
    paisn2= str(input("digite el pais n2: ")).lower()
    golesn2 = int(input("digite los goles del pais n2: "))
    if(paisn1 in semis and paisn2 in semis and goles1 == goles2):
        enfrentamientos(paisn1,golesn1,paisn2,golesn2,faseEnfrentamiento);
    else: i = i - 1
    print(f"equipo de nombre invalido o resultado incorrecto")
     

print(f"los paises clasificados son {finales}")
faseEnfrentamiento = "";

for i in range(1):
    if(paisn1 in finales and paisn2 in finales and goles1 == goles2):
        enfrentamientos(finales[0],golesn1,finales[1],golesn2,faseEnfrentamiento);
    else: i = i - 1
    print(f"equipo de nombre invalido o resultado incorrecto")
 
print(f"el ganador es {faseEnfrentamiento}")

    


