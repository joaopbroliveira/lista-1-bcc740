somatorio = 0
ns = list(range(10))
for i in range(10):
    n1 = float(input("Digite a nota "+ str(i+1) +": "))
    ns[i] = nota
print ("Notas: ", ns)
for x in notas:
    somatorio += x
med = somatorio/len(ns)
print ("Média: ", med)
