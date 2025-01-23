def dia_da_semana(h, d):
    dias = ['Domingo', 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
    index_atual = dias.index(h)
    index_evento = (index_atual + d) % 7
    return dias[index_evento]

lista = list(map(int,input().split()))
x = lista[0] + lista[1]
lista.append(x)
lista.append(x+lista[2])
lista[0] = lista[3] + lista[4]
lista[1] = lista[4] + lista[5]
lista[4] = lista[4] + lista[2]
print(*lista)


lista = list(map(int,input().split()))
x = int(input())
lista.append(x)
t = len(lista)
lista.append(t + lista[2])
lista.append(x+t)
a = len(lista) - 2
print(lista[1], lista[t-1], lista[a])
