# Entrega 7 - Grafo para Soundlink (recomendaciones)
# Canciones conectadas por mismo genero / mismo artista

from collections import deque

class Grafo:
    def __init__(self):
        self.ady = {}  # titulo_lower -> lista de titulos vecinos
        self.por_titulo = {}  # titulo_lower -> cancion

    def agregar_cancion(self, cancion):
        clave = cancion.titulo.lower()
        self.por_titulo[clave] = cancion
        if clave not in self.ady:
            self.ady[clave] = set()

    def conectar(self, titulo1, titulo2):
        t1 = titulo1.lower()
        t2 = titulo2.lower()
        if t1 in self.ady and t2 in self.ady:
            self.ady[t1].add(t2)
            self.ady[t2].add(t1)

    def construir_desde_catalogo(self, catalogo):
        canciones = catalogo.listar()
        for c in canciones:
            self.agregar_cancion(c)
        # Conectar por mismo genero o mismo artista
        for i in range(len(canciones)):
            for j in range(i + 1, len(canciones)):
                a = canciones[i]
                b = canciones[j]
                if getattr(a, 'genero', '') == getattr(b, 'genero', '') or getattr(a, 'artista', '') == getattr(b, 'artista', ''):
                    self.conectar(a.titulo, b.titulo)

    def recomendar(self, titulo, n=3):
        # BFS desde la cancion, devuelve vecinas
        inicio = titulo.lower()
        if inicio not in self.ady:
            return []
        visitados = {inicio}
        cola = deque([inicio])
        resultado = []
        while cola and len(resultado) < n:
            actual = cola.popleft()
            for vecino in self.ady[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
                    resultado.append(self.por_titulo[vecino])
                    if len(resultado) >= n:
                        break
        return resultado