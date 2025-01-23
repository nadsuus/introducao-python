caso = 1

while True:
    try:
        n, r = map(int, input().split())
        retornaram = set(map(int, input().split()))
        nao_retornaram = [i for i in range(1, n + 1) if i not in retornaram]
        
        if not nao_retornaram:
            print("*")
        else:
            print(" ".join(map(str, nao_retornaram)) + " ")
    except EOFError:
        break