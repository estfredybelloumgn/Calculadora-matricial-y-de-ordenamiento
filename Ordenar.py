import random


class Ordenamientos:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.lista_original = []
        self.resultado = []

        for i in range(self.cantidad):
            self.lista_original.append(random.randint(1,10))

    def ordenar(self, opcion):
        lista = self.lista_original.copy()

        if opcion == 1:
            for i in range(len(lista) - 1):
                for j in range(len(lista) - 1 - i):
                    if lista[j] > lista[j + 1]:
                        auxiliar = lista[j]
                        lista[j] = lista[j + 1]
                        lista[j + 1] = auxiliar

            self.resultado = lista

        elif opcion == 2:
            for i in range(1, len(lista)):
                valor_actual = lista[i]
                posicion = i - 1

                while posicion >= 0 and lista[posicion] > valor_actual:
                    lista[posicion + 1] = lista[posicion]
                    posicion = posicion - 1

                lista[posicion + 1] = valor_actual

            self.resultado = lista

        elif opcion == 3:
            for i in range(len(lista) - 1):
                posicion_menor = i

                for j in range(i + 1, len(lista)):
                    if lista[j] < lista[posicion_menor]:
                        posicion_menor = j

                auxiliar = lista[i]
                lista[i] = lista[posicion_menor]
                lista[posicion_menor] = auxiliar

            self.resultado = lista

        elif opcion == 4:
            tamaño = 1

            while tamaño < len(lista):
                inicio = 0

                while inicio < len(lista):
                    mitad = min(inicio + tamaño, len(lista))
                    fin = min(inicio + 2 * tamaño, len(lista))

                    izquierda = lista[inicio:mitad]
                    derecha = lista[mitad:fin]

                    i = 0
                    j = 0
                    k = inicio

                    while i < len(izquierda) and j < len(derecha):
                        if izquierda[i] <= derecha[j]:
                            lista[k] = izquierda[i]
                            i += 1
                        else:
                            lista[k] = derecha[j]
                            j += 1

                        k += 1

                    while i < len(izquierda):
                        lista[k] = izquierda[i]
                        i += 1
                        k += 1

                    while j < len(derecha):
                        lista[k] = derecha[j]
                        j += 1
                        k += 1

                    inicio += 2 * tamaño

                tamaño *= 2

            self.resultado = lista

        elif opcion == 5:
            lista.sort()
            self.resultado = lista

        else:
            self.resultado = []

    def get_lista_original(self):
        return self.lista_original

    def get_resultado(self):
        return self.resultado