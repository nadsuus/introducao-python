caso = 1
while True:
    try:
        n = int(input())
        niveis = list(map(float, input().split())) 
        indices_ordenados = sorted(range(10), key=lambda x: (-niveis[x], x))
        senha = ''.join(map(str, indices_ordenados[:n]))
        print(f"Caso {caso}: {senha}")
        caso += 1
    except EOFError:
        break
