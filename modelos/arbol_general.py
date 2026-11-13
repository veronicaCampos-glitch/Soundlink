# Entrega 5 - Arbol n-ario: Canciones -> Genero
# Un nodo puede tener N hijos, no 2 como el BST/AVL

class NodoGeneral:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []
        self.canciones = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def buscar(self, nombre):
        if self.nombre.lower() == nombre.lower():
            return self
        for h in self.hijos:
            r = h.buscar(nombre)
            if r:
                return r
        return None

def construir_desde_catalogo(catalogo):
    raiz = NodoGeneral("Canciones")
    por_genero = {}
    for cancion in catalogo.listar():
        genero = getattr(cancion, 'genero', 'Sin genero')
        if genero not in por_genero:
            nodo = NodoGeneral(genero)
            por_genero[genero] = nodo
            raiz.agregar_hijo(nodo)
        por_genero[genero].canciones.append(cancion)
    return raiz

def mostrar(nodo, nivel=0):
    print("  " * nivel + "- " + nodo.nombre)
    for c in nodo.canciones:
        print("  " * (nivel + 1) + f"* {c.titulo} - {c.artista}")
    for h in nodo.hijos:
        mostrar(h, nivel + 1)