# Flores Cisneros Adrian Alejandro
# 951
# Se realizó el 23/08/2026
# clase Estadística que contiene como atributo una lista de números naturales la cual puede contener repetidos. Debe contener los siguientes métodos:
# Frecuencia de Números. Dada la lista, devuelve una lista de tuplas con el número de veces que aparece cada número en la lista.
# La tupla debe tener el número y la cantidad de veces que aparece
# Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.
# Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores


class Estadistica:
    def __init__(self,numeros):
        self.numeros = numeros


    def frecuencia_numeros(self):
        frecuencia = {}

        for numero in self.numeros:
            frecuencia[numero] = frecuencia.get(numero,0)+1
        return sorted(frecuencia.items())


    def moda_estadistica(self):
        frecuencia= self.frecuencia_numeros()
        numero_moda, cantidad_max = frecuencia[0]

        for numero, cantidad in frecuencia:

            if cantidad > cantidad_max:
                numero_moda = numero
                cantidad_max= cantidad

        return numero_moda



    def histograma (self):

        for numero, veces in self.frecuencia_numeros():
            print(numero, '*' * veces)




if __name__ == '__main__':
    lista = Estadistica([2,3,1,3,4,5,6,2,3,4,6,8,5,3,3,4,5,1,1])

    print("Frecuencia de Numeros:\n", lista.frecuencia_numeros())

    print("Moda de la lista:\n", lista.moda_estadistica())

    print("Histograma:")
    print(lista.histograma())