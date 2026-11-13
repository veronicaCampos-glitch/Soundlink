# Entrega 6 - Heap para Soundlink (Top canciones)
# El mas escuchado siempre queda arriba

import heapq

class HeapTop:
    def __init__(self):
        self.datos = []

    def agregar(self, cancion):
        # Usamos -reproducciones porque heapq es de minimos
        # y nosotros queremos el maximo arriba
        repro = getattr(cancion, 'rating', 0)
        heapq.heappush(self.datos, (-repro, cancion.titulo.lower(), cancion))

    def top(self, n=5):
        # Devuelve las n mas escuchadas sin romper el heap
        copia = list(self.datos)
        resultado = []
        for _ in range(min(n, len(copia))):
            _, _, cancion = heapq.heappop(copia)
            resultado.append(cancion)
        return resultado

    def mas_escuchada(self):
        if not self.datos:
            return None
        return self.datos[0][2]