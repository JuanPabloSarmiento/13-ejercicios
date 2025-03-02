let numeros = [1,2,3,4,5,6,7,8,9]
let numerosPares = []
for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] % 2 === 0) {
        numerosPares.push(numeros[i])
    }
}
document.write(`numeros pareshasta el ${numeros.length} = ${numerosPares} `)