import time
import numpy as np
import matplotlib.pyplot as plt

inicio = time.time()
tiempo_insertionsort=[]

with open("archivo_1.txt", "r") as file:
    array = eval(file.read())

def insertion_sort(array):
    for i in range(1, len(array)):
        valor_actual = array[i]
        j = i - 1
        while j >= 0 and array[j] > valor_actual:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = valor_actual
    return array

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

fin = time.time()
tiempo = fin - inicio
tiempo_formateado = "{:.3f}".format(tiempo)
tiempo_insertionsort.append(tiempo_formateado)
print("Tiempo de ejecución:", tiempo_formateado, "segundos\n")
##########################################################################
inicio2 = time.time()

with open("archivo_2.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin2 = time.time()
tiempo2 = fin2 - inicio2
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado2 = "{:.3f}".format(tiempo2)
tiempo_insertionsort.append(tiempo_formateado2)
print("Tiempo de ejecución:", tiempo_formateado2, "segundos\n")
##########################################################################
inicio3 = time.time()

with open("archivo_3.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin3 = time.time()
tiempo3 = fin3 - inicio3
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado3 = "{:.3f}".format(tiempo3)
tiempo_insertionsort.append(tiempo_formateado3)
print("Tiempo de ejecución:", tiempo_formateado3, "segundos\n")
##########################################################################
inicio4 = time.time()

with open("archivo_4.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin4 = time.time()
tiempo4 = fin4 - inicio4
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado4 = "{:.3f}".format(tiempo4)
tiempo_insertionsort.append(tiempo_formateado4)
print("Tiempo de ejecución:", tiempo_formateado4, "segundos\n")
##########################################################################
inicio5 = time.time()

with open("archivo_5.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin5 = time.time()
tiempo5 = fin5 - inicio5
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado5 = "{:.3f}".format(tiempo5)
tiempo_insertionsort.append(tiempo_formateado5)
print("Tiempo de ejecución:", tiempo_formateado5, "segundos\n")
##########################################################################
inicio6 = time.time()

with open("archivo_6.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin6 = time.time()
tiempo6 = fin6 - inicio6
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado6 = "{:.3f}".format(tiempo6)
tiempo_insertionsort.append(tiempo_formateado6)
print("Tiempo de ejecución:", tiempo_formateado6, "segundos\n")
##########################################################################
inicio7 = time.time()

with open("archivo_7.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin7 = time.time()
tiempo7 = fin7 - inicio7
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado7 = "{:.3f}".format(tiempo7)
tiempo_insertionsort.append(tiempo_formateado7)
print("Tiempo de ejecución:", tiempo_formateado7, "segundos\n")
##########################################################################
inicio8 = time.time()

with open("archivo_8.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")
# Obtener el tiempo final
fin8 = time.time()
tiempo8 = fin8 - inicio8
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado8 = "{:.3f}".format(tiempo8)
tiempo_insertionsort.append(tiempo_formateado8)
print("Tiempo de ejecución:", tiempo_formateado8, "segundos\n")
##########################################################################
inicio9 = time.time()

with open("archivo_9.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin9 = time.time()
tiempo9 = fin9 - inicio9
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado9 = "{:.3f}".format(tiempo9)
tiempo_insertionsort.append(tiempo_formateado9)
print("Tiempo de ejecución:", tiempo_formateado9, "segundos\n")
##########################################################################
inicio10 = time.time()

with open("archivo_10.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin10 = time.time()
tiempo10 = fin10 - inicio10
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado10 = "{:.3f}".format(tiempo10)
tiempo_insertionsort.append(tiempo_formateado10)
print("Tiempo de ejecución:", tiempo_formateado10, "segundos\n")
##########################################################################
inicio11 = time.time()

with open("archivo_11.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin11 = time.time()
tiempo11 = fin11 - inicio11
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado11 = "{:.3f}".format(tiempo11)
tiempo_insertionsort.append(tiempo_formateado11)
print("Tiempo de ejecución:", tiempo_formateado11, "segundos\n")
##########################################################################
inicio12 = time.time()

with open("archivo_12.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin12 = time.time()
tiempo12 = fin12 - inicio12
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado12 = "{:.3f}".format(tiempo12)
tiempo_insertionsort.append(tiempo_formateado12)
print("Tiempo de ejecución:", tiempo_formateado12, "segundos\n")
##########################################################################
inicio13 = time.time()

with open("archivo_13.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin13 = time.time()
tiempo13 = fin13 - inicio13
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado13 = "{:.3f}".format(tiempo13)
tiempo_insertionsort.append(tiempo_formateado13)
print("Tiempo de ejecución:", tiempo_formateado13, "segundos\n")
##########################################################################
inicio14 = time.time()

with open("archivo_14.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")
# Obtener el tiempo final
fin14 = time.time()
tiempo14 = fin14 - inicio14
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado14 = "{:.3f}".format(tiempo14)
tiempo_insertionsort.append(tiempo_formateado14)
print("Tiempo de ejecución:", tiempo_formateado14, "segundos\n")
##########################################################################
inicio15 = time.time()

with open("archivo_15.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin15 = time.time()
tiempo15 = fin15 - inicio15
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado15 = "{:.3f}".format(tiempo15)
tiempo_insertionsort.append(tiempo_formateado15)
print("Tiempo de ejecución:", tiempo_formateado15, "segundos\n")
##########################################################################
inicio16 = time.time()

with open("archivo_16.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin16 = time.time()
tiempo16 = fin16 - inicio16
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado16 = "{:.3f}".format(tiempo16)
tiempo_insertionsort.append(tiempo_formateado16)
print("Tiempo de ejecución:", tiempo_formateado16, "segundos\n")
##########################################################################
inicio17 = time.time()

with open("archivo_17.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin17 = time.time()
tiempo17 = fin17 - inicio17
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado17 = "{:.3f}".format(tiempo17)
tiempo_insertionsort.append(tiempo_formateado17)
print("Tiempo de ejecución:", tiempo_formateado17, "segundos\n")
##########################################################################
inicio18 = time.time()

with open("archivo_18.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin18 = time.time()
tiempo18 = fin18 - inicio18
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado18 = "{:.3f}".format(tiempo18)
tiempo_insertionsort.append(tiempo_formateado18)
print("Tiempo de ejecución:", tiempo_formateado18, "segundos\n")
##########################################################################
inicio19 = time.time()

with open("archivo_19.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin19 = time.time()
tiempo19 = fin19 - inicio19
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado19 = "{:.3f}".format(tiempo19)
tiempo_insertionsort.append(tiempo_formateado19)
print("Tiempo de ejecución:", tiempo_formateado19, "segundos\n")
##########################################################################
inicio20 = time.time()

with open("archivo_20.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin20 = time.time()
tiempo20 = fin20 - inicio20
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado20 = "{:.3f}".format(tiempo20)
tiempo_insertionsort.append(tiempo_formateado20)
print("Tiempo de ejecución:", tiempo_formateado20, "segundos\n")
##########################################################################
inicio21 = time.time()

with open("archivo_21.txt", "r") as file:
    array = eval(file.read())

#print(array)

insertion_sort(array)
#print("\nLista ordenada: ", array,"\n")

# Obtener el tiempo final
fin21 = time.time()
tiempo21 = fin21 - inicio21
# Formatear el tiempo con una parte entera y tres decimales
tiempo_formateado21 = "{:.3f}".format(tiempo21)
tiempo_insertionsort.append(tiempo_formateado21)
print("Tiempo de ejecución:", tiempo_formateado21, "segundos\n")
##########################################################################

y2 = []
# Abre el archivo en modo lectura
with open('C:\\Users\\USUARIO\\OneDrive\\Escritorio\\codigos_c++\\lista_tiempos_insertionsort.txt', 'r') as archivo:
    # Lee cada línea del archivo
    for linea in archivo:
        # Convierte la línea en un número entero
        numero = int(linea)/1000
        
        # Agrega el número a la lista
        y2.append(numero)

# Imprime la lista de números
print(y2)


y1 = [float(valor) for valor in tiempo_insertionsort]
print("\n",y1,"\n")


# Datos para el gráfico
x1 = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
x2 = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Crear el gráfico lineal con escala logarítmica en el eje x
fig, ax = plt.subplots(figsize=(13, 6))  # Ajusta el ancho y alto según tus necesidades
ax.semilogx(x1,y1, label="Python")
ax.semilogx(x2,y2, label="C++")

# Título del gráfico
ax.set_title('Tiempo de Ejecución - INSERTION SORT')

# Agregar leyenda y etiquetas de los ejes
plt.legend()
plt.xlabel('Cantidad de Archivos')
plt.ylabel('Tiempo (segundos)')

# Ajustar los valores del eje x
ax.set_xticks(x1)
ax.set_xticklabels(x1, rotation=45, fontsize='small')

# Mostrar el gráfico
plt.show()
