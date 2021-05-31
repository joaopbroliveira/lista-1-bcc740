n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = (n1+n2)/2

print("Média: ", n3)
if n3 > 6 :
    print("Aluno aprovado!")
elif n3 >= 4 :
    print("Exame final")
else:
    print("Aluno reprovado!")
