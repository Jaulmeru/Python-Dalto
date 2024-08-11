# Serie de fibonacci desde 0 hasta un numero dado

fibonacci = [0,1]

num_objetivo = int(input("Hasta que numero quieres crear la serie de Fibonacci: "))

while fibonacci[-1] <= num_objetivo:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
fibonacci.pop(-1)

print(fibonacci)