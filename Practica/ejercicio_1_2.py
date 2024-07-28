#a) Pedir al usuario que diga cualquier texto real y
# - calcular cuanto tardaria en decir esa frase (2 palabras x segundo)
# - cuantas palabras dijo

#b) si tarda mas de un minuto decirle "para flaco, tampoco te pedi un testamento"

#c) Dalto habla un 30% mas rapido, cuanto tardaria en decirlo

palabras_por_segundo = 2
texto_usuario = input("Escribeme una frase cualquiera y te digo cuanto te vas a tardar ;)  ")
print("")

#num_palabras = texto_usuario.count(" ") + 1
num_palabras = len(texto_usuario.split(" "))
seg_pronunciacion = num_palabras / palabras_por_segundo

if seg_pronunciacion > 60:
    print(f"Para flaco, tampoco te pedi un testamento. Eso tardaria {seg_pronunciacion} segundos")
elif seg_pronunciacion < 1:
    print("Esa no es un frase, no me quieras hacer wey")
else:
    print(f"En decir todo eso te tardarias {seg_pronunciacion} segundos")
    print(f"Fueron en total {num_palabras} palabras")
    print("")
    print(f"Dalto que es un chiflado y habla 30% mas rapido se tardaria {round(70/100*seg_pronunciacion,2)} segundos")
