saldo = 1000
puts 'Ingrese monto a retirar:'
monto = gets.to_i
puts saldo >= monto ? 'Retiro exitoso' : 'Saldo insuficiente'