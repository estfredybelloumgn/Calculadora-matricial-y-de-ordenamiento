from CalcMatrices import CalcMatrix
from Ordenar import Ordenamientos
CalcM = CalcMatrix([],[],[],[])
Order = Ordenamientos(0)

def main():
    continuar="s"
    while (continuar=="s"):
        print("\n-----------CALCULADORA-----------")
        print("|1.Operaciones con matrices       |")
        print("|2.Ordenamiento                   |")
        print("|3. SALIR                         |")
        print("-----------------------------------")

        opcion_principal=int(input("\n----Escoja una de las opciones: "))
        if opcion_principal==1:
            print("\n------Operaciones con matrices------")
            print("1. Suma de matrices \n2. producto de matrices \n3. Inversa de una matriz \n4. Producto de una matriz por un vector")
            opcion=int(input("Escoja una de las opciones: "))
           
            if opcion==1:
                CalcM.pedirM_A()
                CalcM.pedirM_B()
                CalcM.suma_matrices()
                resultado= CalcM.get_resultado()
                print(resultado)
            elif opcion==2:
                CalcM.pedirM_A()
                CalcM.pedirM_B()
                CalcM.producto_matrices()
                resultado= CalcM.get_resultado()
                print(resultado)
            elif opcion==3:
                CalcM.pedirM_A()
                CalcM.inversa_matriz()
                resultado= CalcM.get_resultado()
                print(resultado)
            elif opcion==4:
                CalcM.pedirM_A()
                CalcM.pedirVect()
                CalcM.producto_matriz_vector()
                resultado= CalcM.get_resultado()
                print(resultado)
            else:
                print("ERROR: Operación no valida")
        elif opcion_principal == 2:
            cantidad = int(input("\n¿Cuántos números aleatorios desea generar?: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
            else:
                ordenar = Ordenamientos(cantidad)

                print("\nLista original:")
                print(ordenar.get_lista_original())

                print("\n------ MÉTODOS DE ORDENAMIENTO ------")
                print("1. Método burbuja")
                print("2. Método inserción")
                print("3. Método selección")
                print("4. Método merge sort")
                print("5. Método sort de Python")

                opcion_ordenamiento = int(input("\nSeleccione el método de ordenamiento: "))

                if opcion_ordenamiento >= 1 and opcion_ordenamiento <= 5:
                    ordenar.ordenar(opcion_ordenamiento)

                    print("\nLista ordenada:")
                    print(ordenar.get_resultado())
                else:
                    print("Error: opción de ordenamiento no válida.")
        elif opcion_principal == 3:
            print("\nPrograma finalizado.")
            continuar = "n"
        else:
            print("\nError: opción principal no válida.")
        

if __name__ == "__main__":
    main()
