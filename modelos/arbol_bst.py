class Nodo:
    def __init__(self, cancion):
        self.clave = cancion.titulo.lower()
        self.cancion = cancion
        self.izq = None
        self.der = None

class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, cancion):
        if self.raiz is None:
            self.raiz = Nodo(cancion)
        else:
            self._insertar(self.raiz, cancion)

    def _insertar(self, nodo, cancion):
        clave = cancion.titulo.lower()
        if clave < nodo.clave:
            if nodo.izq is None:
                nodo.izq = Nodo(cancion)
            else:
                self._insertar(nodo.izq, cancion)
        else:
            if nodo.der is None:
                nodo.der = Nodo(cancion)
            else:
                self._insertar(nodo.der, cancion)

    def buscar(self, titulo):
        return self._buscar(self.raiz, titulo.lower())

    def _buscar(self, nodo, titulo):
        if nodo is None:
            return None
        if titulo == nodo.clave:
            return nodo.cancion
        if titulo < nodo.clave:
            return self._buscar(nodo.izq, titulo)
        return self._buscar(nodo.der, titulo)

    def inorder(self):
        lista = []
        self._inorder(self.raiz, lista)
        return lista

    def _inorder(self, nodo, lista):
        if nodo:
            self._inorder(nodo.izq, lista)
            lista.append(nodo.cancion)
            self._inorder(nodo.der, lista)