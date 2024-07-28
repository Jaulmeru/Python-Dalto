#Diferencia porcentual entre el curso actual y el mas rapido, el mas lento y el promedio de los otros cursos
actual = 1.5
rapido = 2.5
lento = 7
promedio = 4

print("------------------------------------")
print(f"Este curso es {round(100-(actual*100/rapido),2)}% mas rapido que el mas rapido de los otros cursos")
print(f"Este curso es {round(100-(actual*100/promedio),2)}% mas rapido que el promedio de los otros cursos")
print(f"Este curso es {round(100-(actual*100/lento),2)}% mas rapido que el mas lento de los otros cursos")

#Porcentaje de material inservible que se reduce en el promedio de cursos y el actual
actual_crudo = 3.5
promedio_crudo = 5

print("------------------------------------")
print(f"Este curso redujo {round(100-(actual*100/actual_crudo),2)}% del contenido crudo")
print(f"Los otros cursos en promedio redujeron {round(100-(promedio*100/promedio_crudo),2)}% del contenido crudo")

# A cuantas horas de otros cursos equivale ver 10 horas de este curso
print("------------------------------------")
print(f"Ver 10 horas de este curso equivale a ver {round(10/actual*promedio,2)} horas de otros cursos")
print(f"Y ver 10 horas de otros cursos equivale a ver {round(10/promedio*actual,2)} horas de este curso")
print("------------------------------------")