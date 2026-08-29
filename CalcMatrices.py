class CalcMatrix:
    def __init__(self, matrizA, matrizB, vectorU, resultado):
        self.matrizA = matrizA
        self.matrizB = matrizB
        self.vectorU = vectorU
        self.resultado = resultado

    def pedirM_A(self):
        filas = int(input("Ingrese el número de filas para la matriz A: "))
        columnas = int(input("Ingrese el número de columnas para la matriz A: "))
        self.matrizA=[]
        print("A continuación ingrese los valores de la matriz en la respectiva posición mostrada")
        for i in range (filas):
            fila=[]
            for j in range (columnas):
                valor= int(input(f"A[{i}][{j}]:"))
                fila.append(valor)
            self.matrizA.append(fila)
        print("\nMatriz A:")
        for fila in self.matrizA:
            for valor in fila:
                print(f"{valor}", end="\t")
            print()

    def pedirM_B(self):
        filas = int(input("Ingrese el número de filas para la matriz B: "))
        columnas = int(input("Ingrese el número de columnas para la matriz B: "))
        self.matrizB=[]
        print("A continuación ingrese los valores de la matriz en la respectiva posición mostrada")
        for i in range (filas):
            fila=[]
            for j in range (columnas):
                valor= int(input(f"B[{i}][{j}]:"))
                fila.append(valor)
            self.matrizB.append(fila)
        print("\nMatriz B:")
        for fila in self.matrizB:
            for valor in fila:
                print(f"{valor}", end="\t")
            print()

    def pedirVect(self):
        cantidad=int(input("Ingrese la cantidad de elementos del vector: "))
        self.vectorU=[]

        for i in range (cantidad):
            valor=int(input(f"Vector[{i}]: "))
            self.vectorU.append(valor)

        print("\nVector ingresado: ")
        print(self.vectorU)

    def suma_matrices(self):
        filasA = len(self.matrizA)
        columnasA = len(self.matrizA[0])
        filasB = len(self.matrizB)
        columnasB = len(self.matrizB[0])
        self.resultado=[]
        if filasA != filasB or columnasA != columnasB:
            self.resultado = ("No se pueden sumar matrices con distintas dimensiones")
            return

        else:
            for i in range (filasA):
                fila=[]
                for j in range (columnasA):
                    valor= self.matrizA[i][j]+self.matrizB[i][j]
                    fila.append(valor)
                self.resultado.append(fila)
            print("\nResultado: ")

    def producto_matrices(self):
        filasA = len(self.matrizA)
        columnasA = len(self.matrizA[0])
        filasB = len(self.matrizB)
        columnasB = len(self.matrizB[0])
        
        if columnasA != filasB:
            self.resultado = "No se pueden multiplicar las matrices: las columnas de A deben ser iguales a las filas de B."
            return
        else:
            self.resultado=[]
            for i in range (filasA):
                fila=[]
                for j in range (columnasB):
                    suma = 0
                    for k in range (columnasA):
                        suma += self.matrizA[i][k]*self.matrizB[k][j]
                    fila.append(suma)
                self.resultado.append(fila)

    def producto_matriz_vector(self):
        filas = len(self.matrizA)
        columnas = len(self.matrizA[0])

        if columnas != len(self.vectorU):
            self.resultado = ("La cantidad de elementos del vector debe coincidir con las columnas de A.")
            return

        self.resultado = []

        for i in range(filas):
            suma = 0
            for j in range(columnas):
                suma += self.matrizA[i][j] * self.vectorU[j]
            self.resultado.append(suma)

    def inversa_matriz(self):
        n=len(self.matrizA)
       
        if any(len(fila)!=n for fila in self.matrizA):
            self.resultado = ("La matriz debe ser cuadrada para calcular su inversa")

        else: 
            aumentada=[]
            for i in range (n):
                fila=[]
                for j in range (n):
                    fila.append(int(self.matrizA[i][j]))
                for j in range (n):
                    if i==j:
                        fila.append(1)
                    else:
                        fila.append(0)
                aumentada.append(fila)
            
            for columna in range (n):
                pivote=columna
                for fila in range (columna+1, n):
                    if abs (aumentada[fila][columna])> abs(aumentada[pivote][columna]):
                        pivote=fila
                if abs(aumentada[pivote][columna])< 1e-12:
                    self.resultado= "LA matriz no tiene inversa porque es singular"
                    return

                if pivote != columna:
                    aumentada[columna], aumentada[pivote] = aumentada[pivote], aumentada[columna]

                valor_pivote = aumentada[columna][columna]

                for j in range(2 * n):
                    aumentada[columna][j] /= valor_pivote

                for fila in range(n):
                    if fila != columna:
                        factor = aumentada[fila][columna]

                        for j in range(2 * n):
                            aumentada[fila][j] -= (factor * aumentada[columna][j])

            self.resultado = []
            for i in range(n):
                fila = []
                for j in range(n, 2 * n):
                    valor = aumentada[i][j]
                    if abs(valor) < 1e-12:
                        valor = 0
                    fila.append(valor)
                self.resultado.append(fila)

    def get_resultado(self):
        return self.resultado

        