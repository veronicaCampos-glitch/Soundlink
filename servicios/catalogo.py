import json
from modelos.cancion import Cancion

class Catalogo:
    """Logica de negocio: carga y operaciones sobre el catalogo de canciones."""

    def __init__(self) -> None:
        self._canciones: list[Cancion] = []

    def cargar_desde_json(self, ruta: str) -> None:
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for d in datos:
                self._canciones.append(
                    Cancion(d["titulo"], d["artista"], d["genero"], d["anio"], d["rating"], d["colaboraciones"])
                )

    def buscar(self, titulo: str):
        """Busqueda por titulo, sin distinguir mayusculas."""
        for c in self._canciones:
            if titulo.lower() in c.titulo.lower():
                return c
        return None

    def listar(self) -> list[Cancion]:
        return list(self._canciones)

    def filtrar(self, genero: str) -> list[Cancion]:
        return [c for c in self._canciones if c.genero.lower() == genero.lower()]

    def __len__(self) -> int:
        return len(self._canciones)
