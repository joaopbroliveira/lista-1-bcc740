n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3=[n1, n2]
med = sum(n3)/2
print("Média: ", med)
if med >=6 :
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")
