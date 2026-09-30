import json
from modelos.cancion import Cancion
from modelos.arbol_bst import ArbolBST
import time

class Catalogo:
    """Logica de negocio: carga y operaciones sobre el catalogo de canciones."""

    def __init__(self) -> None:
        self._canciones: list[Cancion] = []
        self._arbol = ArbolBST() # Nuevo para TP3
        self._indice_construido = False

    def cargar_desde_json(self, ruta: str) -> None:
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for d in datos:
                self._canciones.append(
                    Cancion(d["titulo"], d["artista"], d["genero"], d["anio"], d["rating"], d["colaboraciones"])
                )
        # Construimos el arbol automaticamente al cargar - TP3
        self.construir_indice_bst()

    def buscar(self, titulo: str):
        """Busqueda por titulo, sin distinguir mayusculas. TP2 - O(n)"""
        for c in self._canciones:
            if titulo.lower() in c.titulo.lower():
                return c
        return None

    # --- NUEVO TP2 Y TP3 ---

    def construir_indice_bst(self):
        self._arbol = ArbolBST()
        for c in self._canciones:
            self._arbol.insertar(c)
        self._indice_construido = True

    def buscar_secuencial_exacta(self, titulo: str):
        """Estrategia 1: O(n) exacta"""
        titulo = titulo.lower()
        for c in self._canciones:
            if c.titulo.lower() == titulo:
                return c
        return None

    def buscar_con_arbol(self, titulo: str):
        """Estrategia 2: O(log n) promedio con BST - TP3"""
        if not self._indice_construido:
            self.construir_indice_bst()
        return self._arbol.buscar(titulo)

    def comparar_estrategias(self, titulo: str):
        """TP2 - Devuelve tiempos para la tabla"""
        t1 = time.perf_counter()
        self.buscar_secuencial_exacta(titulo)
        t_sec = (time.perf_counter() - t1) * 1000

        t2 = time.perf_counter()
        self.buscar_con_arbol(titulo)
        t_bst = (time.perf_counter() - t2) * 1000
        return t_sec, t_bst

    def listar_ordenado(self):
        """TP3 - Inorder del arbol"""
        return self._arbol.inorder()

    # --- Lo tuyo original que no se toca ---
    def listar(self) -> list[Cancion]:
        return list(self._canciones)

    def filtrar(self, genero: str) -> list[Cancion]:
        return [c for c in self._canciones if c.genero.lower() == genero.lower()]

    def __len__(self) -> int:
        return len(self._canciones)
