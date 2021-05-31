from calculadora import calculadora1

x = calculadora1(10,5)

print("Soma: ", x.soma())
print("Subtração: ", x.subtrai())
print("Multiplicação: ", x.multiplica())
print("Divisão: ", x.divide())

x.a = 50
x.b = 10

print(x.a," + ", x.b , " = ", x.soma())
print(x.a, " - ", x.b, " = ", x.subtrai())
print(x.a , " x ", x.b, " = ", x.multiplica())
print(x.a, " / ", x.b, " = ", x.divide())
