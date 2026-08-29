from CalcMatrices import CalcMatrix

CalcM = CalcMatrix([],[],[],[])

continuar="s"
def main():
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


if __name__ == "__main__":
    main()
