sentence = "Practice Problems to Drill List Comprehension in Your Head."

lista1 = list(sentence)

[lista.remove(i) for i in lista1 if i == "a"]
[lista.remove(i) for i in lista1 if i == "e"]
[lista.remove(i) for i in lista1 if i == "i"]
[lista.remove(i) for i in lista1 if i == "o"]
[lista.remove(i) for i in lista1 if i == "u"]

print(lista1)
