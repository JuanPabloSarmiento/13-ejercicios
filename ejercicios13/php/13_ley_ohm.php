<?php
function calcularOhm($voltaje, $resistencia) {
    return $voltaje / $resistencia;
}

$voltaje = 10;
$resistencia = 5;
$intensidad = calcularOhm($voltaje, $resistencia);
echo "La corriente es: $intensidad A";
?>