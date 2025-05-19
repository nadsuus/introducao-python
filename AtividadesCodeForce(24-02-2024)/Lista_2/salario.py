nome = input();
numero = int(input());
valorDaHoraTrabalhada = float(input());

calculoDeHoras = numero * valorDaHoraTrabalhada;

print(nome)
print("R$ "f"{calculoDeHoras:.2f}")
