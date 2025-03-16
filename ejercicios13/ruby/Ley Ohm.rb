puts 'Ingrese voltaje y resistencia:'
v, r = gets.split.map(&:to_f)
puts 'Corriente: #{v / r}'