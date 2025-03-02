const carros = [
    { marca: 'Fiat', modelo: 'Uno', año: 1999 },
    { marca: 'Chevrolet', modelo: 'Celta', año: 2001},
    { marca: 'Fiat', modelo: 'Palio', año: 2003 },
    { marca: 'Chevrolet', modelo: 'Cruze', año: 2005}
]
let valoresRepetidos = new Set();
carros.forEach(elemento => {
    if (!valoresRepetidos.has(elemento.marca)) {
        document.write(` ${elemento.marca} <br>`)
        valoresRepetidos.add(elemento.marca)
    }
   })