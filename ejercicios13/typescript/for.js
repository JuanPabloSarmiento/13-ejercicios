let lista1 = [nombre,apellido,edad,lista]
document.write(`<b> Datos usados hasta ahora </b><br>`)
for (let i = 0; i < lista1.length; i++) {
    if (i == lista1.length){
        document.write(`este es el ultimo dato generado ${lista1[i]} <br>`)
    }
    else {
        document.write(`${lista1[i]} <br>`)
    }
}