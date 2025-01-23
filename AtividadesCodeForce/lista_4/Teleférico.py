c = int(input()) 
a = int(input())  

capacidade_alunos = c - 1
viagens = (a + capacidade_alunos - 1) // capacidade_alunos
print(viagens)
