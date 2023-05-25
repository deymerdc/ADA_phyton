import random
# Ejemplo de uso


def generar_lista_aleatoria(n):
    numeros = list(range(1, n+1))
    random.shuffle(numeros)
    return numeros

i=100
for n in range(21):
    if (i<=100):
        print("\nTamaño de la lista: ", i)
        lista_aleatoria = generar_lista_aleatoria(i)
        archivo1 = open("archivo_1.txt","w")
        a = str(lista_aleatoria)
        archivo1.write(a)
        i=i+400

    elif i==500:
        print("\nTamaño de la lista: ", i)
        lista_aleatoria = generar_lista_aleatoria(i)
        archivo2 = open("archivo_2.txt","w")
        b = str(lista_aleatoria)
        archivo2.write(b)
        i=i+500

    elif 1000<=i<=9999:
        print("\nTamaño de la lista: ", i)
        lista_aleatoria = generar_lista_aleatoria(i)
        if i==1000:
            archivo3 = open("archivo_3.txt","w")
            c = str(lista_aleatoria)
            archivo3.write(c)

        elif i==2000:
            archivo4 = open("archivo_4.txt","w")
            d = str(lista_aleatoria)
            archivo4.write(d)

        elif i==3000:
            archivo5 = open("archivo_5.txt","w")
            e = str(lista_aleatoria)
            archivo5.write(e)

        elif i==4000:
            archivo6 = open("archivo_6.txt","w")
            f = str(lista_aleatoria)
            archivo6.write(f)

        elif i==5000:
            archivo7 = open("archivo_7.txt","w")
            h = str(lista_aleatoria)
            archivo7.write(h)

        elif i==6000:
            archivo8 = open("archivo_8.txt","w")
            g = str(lista_aleatoria)
            archivo8.write(g)

        elif i==7000:
            archivo9 = open("archivo_9.txt","w")
            j = str(lista_aleatoria)
            archivo9.write(j)

        elif i==8000:
            archivo10 = open("archivo_10.txt","w")
            k = str(lista_aleatoria)
            archivo10.write(k)

        elif i==9000:
            archivo11 = open("archivo_11.txt","w")
            l = str(lista_aleatoria)
            archivo11.write(l)

        if 1000<=i<9999:
            i=i+1000
        else:
            i=i

    elif 10000<=i<=100000:
        print("\nTamaño de la lista: ", i)
        lista_aleatoria = generar_lista_aleatoria(i)

        if i==10000:
            archivo12 = open("archivo_12.txt","w")
            m = str(lista_aleatoria)
            archivo12.write(m)

        elif i==20000:
            archivo13 = open("archivo_13.txt","w")
            n = str(lista_aleatoria)
            archivo13.write(n)

        elif i==30000:
            archivo14 = open("archivo_14.txt","w")
            o = str(lista_aleatoria)
            archivo14.write(o)

        elif i==40000:
            archivo15 = open("archivo_15.txt","w")
            p = str(lista_aleatoria)
            archivo15.write(p)

        elif i==50000:
            archivo16 = open("archivo_16.txt","w")
            q = str(lista_aleatoria)
            archivo16.write(q)

        elif i==60000:
            archivo17 = open("archivo_17.txt","w")
            r = str(lista_aleatoria)
            archivo17.write(r)

        elif i==70000:
            archivo18 = open("archivo_18.txt","w")
            s = str(lista_aleatoria)
            archivo18.write(s)

        elif i==80000:
            archivo19 = open("archivo_19.txt","w")
            t = str(lista_aleatoria)
            archivo19.write(t)

        elif i==90000:
            archivo20 = open("archivo_20.txt","w")
            u = str(lista_aleatoria)
            archivo20.write(u)
        
        elif i==100000:
            archivo21 = open("archivo_21.txt","w")
            v = str(lista_aleatoria)
            archivo21.write(v)

        i=i+10000







