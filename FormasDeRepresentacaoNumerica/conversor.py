def exibir_opcoes():
    print("Escolha um número para a forma de entrada desejada:")
    print("1 -------------- Binário --------------")
    print("2 -------------- Natural --------------")
    print("3 ---------- Sinal-Magnitude ----------")
    print("4 -------- Complemento de dois --------")
    print("5 ------------ Ponto Fixo -------------")
    print("6 ---------- Ponto Flutuante ----------")

def opcoes_de_escolha():
    while True:
        exibir_opcoes()
        try:
            escolha = int(input("Digite sua escolha: "))

            if escolha < 1 or escolha > 6:
                print("Escolha uma opção válida entre 1 e 6.")
            else:
                return escolha
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 6.")

def binario_para_decimal(binario):
    return int(binario, 2)

def decimal_para_binario(decimal):
    binario = bin(abs(decimal))[2:]  # Remove o prefixo '0b'
    return binario.zfill(12)  # Ajusta para 12 bits

def complemento_de_dois_para_binario(decimal):
    if decimal >= 0:
        return decimal_para_binario(decimal)
    else:
        binario = decimal_para_binario(-decimal)
        invertido = ''.join('1' if bit == '0' else '0' for bit in binario)
        soma_um = bin(int(invertido, 2) + 1)[2:]  # Soma 1 e ajusta
        return soma_um.zfill(12)

def complemento_de_dois(binario):
    if binario[0] == "0":
        return binario_para_decimal(binario)
    else:
        invertido = ''.join('1' if bit == '0' else '0' for bit in binario)
        soma_um = binario_para_decimal(invertido) + 1
        return -soma_um

def binario_para_sinal_magnitude(binario):
    sinal = "-" if binario[0] == "1" else ""
    magnitude_decimal = binario_para_decimal(binario[1:])
    return sinal, magnitude_decimal

def binario_para_ponto_fixo(binario):
    # Certificar-se de que o binário possui o formato correto
    binario = binario.zfill(12)
    
    # Separar o sinal, parte inteira e parte fracionária
    sinal = -1 if binario[0] == "1" else 1
    parte_inteira = binario_para_decimal(binario[1:6])  # 5 bits para a parte inteira
    parte_fracionaria_bin = binario[6:]  # 6 bits para a parte fracionária
    
    # Converter parte fracionária
    parte_fracionaria = sum(int(bit) * (2 ** -(i + 1)) for i, bit in enumerate(parte_fracionaria_bin))
    
    # Calcular o ponto fixo
    ponto_fixo = sinal * (parte_inteira + parte_fracionaria)
    return ponto_fixo


def ponto_fixo_para_binario(ponto_fixo):
    # Determinar o sinal
    sinal = "0" if ponto_fixo >= 0 else "1"
    ponto_fixo = abs(ponto_fixo)

    # Parte inteira
    parte_inteira = int(ponto_fixo)
    parte_inteira_bin = bin(parte_inteira)[2:].zfill(5)  # Ajusta para 5 bits

    # Parte fracionária
    parte_fracionaria = ponto_fixo - parte_inteira
    parte_fracionaria_bin = ""
    for _ in range(6):  # 6 bits para a parte fracionária
        parte_fracionaria *= 2
        if parte_fracionaria >= 1:
            parte_fracionaria_bin += "1"
            parte_fracionaria -= 1
        else:
            parte_fracionaria_bin += "0"

    # Combinar sinal, parte inteira e parte fracionária com o ponto
    return f"{sinal}{parte_inteira_bin}.{parte_fracionaria_bin}"


def binario_para_ponto_flutuante(binario):
    binario = binario.zfill(12)
    sinal = -1 if binario[0] == "1" else 1
    expoente_bin = binario[1:6]
    mantissa_bin = binario[6:]
    expoente = complemento_de_dois(expoente_bin)
    mantissa = sum(int(bit) * (2 ** -(i + 1)) for i, bit in enumerate(mantissa_bin))
    ponto_flutuante = sinal * (1 + mantissa) * (2 ** expoente)
    return ponto_flutuante

def ponto_flutuante_para_binario(ponto_flutuante):
    sinal = "0" if ponto_flutuante >= 0 else "1"
    ponto_flutuante = abs(ponto_flutuante)

    # Decompor em 1.mmmmmm * 2^e
    expoente = 0
    while ponto_flutuante >= 2:
        ponto_flutuante /= 2
        expoente += 1
    while ponto_flutuante < 1:
        ponto_flutuante *= 2
        expoente -= 1

    mantissa = ponto_flutuante - 1

    # Converter expoente para complemento de dois
    expoente_bin = complemento_de_dois_para_binario(expoente)[-5:]  # Ajusta para 5 bits

    # Converter mantissa para binário
    mantissa_bin = ""
    for _ in range(6):
        mantissa *= 2
        if mantissa >= 1:
            mantissa_bin += "1"
            mantissa -= 1
        else:
            mantissa_bin += "0"

    return sinal + expoente_bin + mantissa_bin

# Fluxo principal
if __name__ == "__main__":
    escolha = opcoes_de_escolha()

    if escolha == 1:
        valor_entrada = input("Digite o valor da entrada em binário: ")
        if not all(bit in '01' for bit in valor_entrada):
            print("Erro: Entrada inválida. Certifique-se de fornecer um número binário válido.")
        else:
            print(f"Dado de entrada *Binário*: {valor_entrada}")

            # Determinar os valores a partir do binário
            natural = binario_para_decimal(valor_entrada)
            sinal, magnitude_decimal = binario_para_sinal_magnitude(valor_entrada)
            complemento_de_dois_valor = complemento_de_dois(valor_entrada)
            ponto_fixo_valor = binario_para_ponto_fixo(valor_entrada)
            ponto_flutuante_valor = binario_para_ponto_flutuante(valor_entrada)

            print(f"Natural: {natural}")
            print(f"Sinal-Magnitude: {sinal}{magnitude_decimal}")
            print(f"Complemento de Dois: {complemento_de_dois_valor}")
            print(f"Ponto Fixo: {ponto_fixo_valor}")
            print(f"Ponto Flutuante: {ponto_flutuante_valor}")

    elif escolha == 2:
        valor_entrada = int(input("Digite o valor da entrada: "))
        print(f"Dado de entrada *Natural*: {valor_entrada}")

        # Determinar binário
        binario = decimal_para_binario(valor_entrada)
        print(f"Binário: {binario}")

        # Determinar complemento de dois
        complemento_decimal = complemento_de_dois(binario)
        print(f"Complemento de Dois (Decimal): {complemento_decimal}")

        # Determinar sinal-magnitude
        sinal, magnitude = binario_para_sinal_magnitude(binario)
        print(f"Sinal-Magnitude: {sinal}{magnitude}")

        # Determinar ponto fixo
        ponto_fixo_valor = binario_para_ponto_fixo(binario)
        print(f"Ponto Fixo: {ponto_fixo_valor}")

        # Determinar ponto flutuante
        ponto_flutuante_valor = binario_para_ponto_flutuante(binario)
        print(f"Ponto Flutuante: {ponto_flutuante_valor}")

    elif escolha == 3:
        valor_entrada = int(input("Digite o valor da entrada: "))
        print(f"Dado de entrada *Sinal-Magnitude*: {valor_entrada}")

        # Determinar binário no formato Sinal-Magnitude
        sinal = "1" if valor_entrada < 0 else "0"  # Sinal: 1 para negativo, 0 para positivo
        magnitude = abs(valor_entrada)
        
        # Ajustar a magnitude para 11 bits exatamente
        magnitude_binario = bin(magnitude)[2:].zfill(11)  # Remove o prefixo '0b' e ajusta para 11 bits
        
        # Combinar sinal e magnitude
        sinal_magnitude_binario = sinal + magnitude_binario
        print(f"Binário (Sinal-Magnitude): {sinal_magnitude_binario}")

        # Determinar o natural a partir do binário
        natural = binario_para_decimal(sinal_magnitude_binario[1:])  # Ignora o bit de sinal
        print(f"Natural: {natural}")

        # Determinar complemento de dois
        complemento_de_dois_valor = complemento_de_dois(sinal_magnitude_binario)
        print(f"Complemento de Dois: {complemento_de_dois_valor}")

        # Determinar ponto fixo
        ponto_fixo_valor = binario_para_ponto_fixo(sinal_magnitude_binario)
        print(f"Ponto Fixo: {ponto_fixo_valor}")

        # Determinar ponto flutuante
        ponto_flutuante_valor = binario_para_ponto_flutuante(sinal_magnitude_binario)
        print(f"Ponto Flutuante: {ponto_flutuante_valor}")



    elif escolha == 4:
        valor_entrada = int(input("Digite o valor da entrada: "))
        print(f"Dado de entrada *Complemento de Dois*: {valor_entrada}")

        # Determinar o binário no formato Complemento de Dois
        binario_complemento = complemento_de_dois_para_binario(valor_entrada)
        print(f"Binário (Complemento de Dois): {binario_complemento}")

        # Determinar o natural a partir do binário
        natural = binario_para_decimal(binario_complemento[1:])  # Ignora o bit de sinal
        print(f"Natural: {natural}")

        # Determinar Sinal-Magnitude
        sinal, magnitude = binario_para_sinal_magnitude(binario_complemento)
        print(f"Sinal-Magnitude: {sinal}{magnitude}")

        # Determinar ponto fixo
        ponto_fixo_valor = binario_para_ponto_fixo(binario_complemento)
        print(f"Ponto Fixo: {ponto_fixo_valor}")

        # Determinar ponto flutuante
        ponto_flutuante_valor = binario_para_ponto_flutuante(binario_complemento)
        print(f"Ponto Flutuante: {ponto_flutuante_valor}")


    elif escolha == 5:
        valor_entrada = float(input("Digite o valor da entrada em ponto fixo: "))
        print(f"Dado de entrada *Ponto Fixo*: {valor_entrada}")

        # Determinar binário a partir do ponto fixo
        binario_ponto_fixo = ponto_fixo_para_binario(valor_entrada)
        print(f"Binário: {binario_ponto_fixo}")

        # Determinar o valor natural
        natural = binario_para_decimal(binario_ponto_fixo)
        print(f"Natural: {natural}")

        # Conversão para sinal-magnitude
        sinal, magnitude_decimal = binario_para_sinal_magnitude(binario_ponto_fixo)
        print(f"Sinal-Magnitude: {sinal}{magnitude_decimal}")

        # Conversão para complemento de dois
        complemento_de_dois_valor = complemento_de_dois(binario_ponto_fixo)
        print(f"Complemento de Dois: {complemento_de_dois_valor}")

        # Conversão para ponto flutuante
        ponto_flutuante_valor = binario_para_ponto_flutuante(binario_ponto_fixo)
        print(f"Ponto Flutuante: {ponto_flutuante_valor}")

    elif escolha == 6:
        valor_entrada = float(input("Digite o valor da entrada em ponto flutuante: "))
        print(f"Dado de entrada *Ponto Flutuante*: {valor_entrada}")

        # Determinar binário a partir do ponto flutuante
        binario_ponto_flutuante = ponto_flutuante_para_binario(valor_entrada)
        print(f"Binário: {binario_ponto_flutuante}")

        # Determinar o valor natural
        natural = binario_para_decimal(binario_ponto_flutuante)
        print(f"Natural: {natural}")

        # Conversão para sinal-magnitude
        sinal, magnitude_decimal = binario_para_sinal_magnitude(binario_ponto_flutuante)
        print(f"Sinal-Magnitude: {sinal}{magnitude_decimal}")

        # Conversão para complemento de dois
        complemento_de_dois_valor = complemento_de_dois(binario_ponto_flutuante)
        print(f"Complemento de Dois: {complemento_de_dois_valor}")

        # Conversão para ponto fixo
        ponto_fixo_valor = binario_para_ponto_fixo(binario_ponto_flutuante)
        print(f"Ponto Fixo: {ponto_fixo_valor}")
