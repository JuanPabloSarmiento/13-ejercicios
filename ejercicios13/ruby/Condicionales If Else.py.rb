puts 'Ingrese un número:'
n = gets.to_i
puts n > 0 ? 'Positivo' : (n < 0 ? 'Negativo' : 'Cero')