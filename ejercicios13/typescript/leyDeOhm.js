function calcularOhm() {
    let opcion = prompt(`Ley de Ohm: ¿Qué desea hallar?\n1. Voltaje (V)\n2. Corriente (I)\n3. Resistencia (R)`);

    if (opcion === "1") {
        let I = parseFloat(prompt("Ingrese la corriente (A):"));
        let R = parseFloat(prompt("Ingrese la resistencia (Ω):"));
        if (!isNaN(I) && !isNaN(R)) {
            let V = I * R;
            alert(`El voltaje es: ${V} V`);
        } else {
            alert("Por favor, ingrese valores numéricos válidos.");
        }
    } 
    else if (opcion === "2") {
        let V = parseFloat(prompt("Ingrese el voltaje (V):"));
        let R = parseFloat(prompt("Ingrese la resistencia (Ω):"));
        if (!isNaN(V) && !isNaN(R) && R !== 0) {
            let I = V / R;
            alert(`La corriente es: ${I} A`);
        } else {
            alert("Por favor, ingrese valores numéricos válidos y asegúrese de que R no sea 0.");
        }
    } 
    else if (opcion === "3") {
        let V = parseFloat(prompt("Ingrese el voltaje (V):"));
        let I = parseFloat(prompt("Ingrese la corriente (A):"));
        if (!isNaN(V) && !isNaN(I) && I !== 0) {
            let R = V / I;
            alert(`La resistencia es: ${R} Ω`);
        } else {
            alert("Por favor, ingrese valores numéricos válidos y asegúrese de que I no sea 0.");
        }
    } 
    else {
        alert("Opción no válida. Intente de nuevo.");
    }
}


calcularOhm();