# Entrega 4 - AVL para Soundlink (canciones)
# Mismo uso que el BST de TP3, pero balanceado

class NodoAVL:
    def __init__(self, cancion):
        self.cancion = cancion
        self.clave = cancion.titulo.lower()
        self.izq = None
        self.der = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _altura(self, n):
        return n.altura if n else 0

    def _balance(self, n):
        return self._altura(n.izq) - self._altura(n.der) if n else 0

    def _actualizar(self, n):
        n.altura = 1 + max(self._altura(n.izq), self._altura(n.der))

    def _rotar_der(self, y):
        x = y.izq
        t = x.der
        x.der = y
        y.izq = t
        self._actualizar(y)
        self._actualizar(x)
        return x

    def _rotar_izq(self, x):
        y = x.der
        t = y.izq
        y.izq = x
        x.der = t
        self._actualizar(x)
        self._actualizar(y)
        return y

    def _insertar(self, nodo, cancion):
        if not nodo:
            return NodoAVL(cancion)
        clave = cancion.titulo.lower()
        if clave < nodo.clave:
            nodo.izq = self._insertar(nodo.izq, cancion)
        elif clave > nodo.clave:
            nodo.der = self._insertar(nodo.der, cancion)
        else:
            return nodo

        self._actualizar(nodo)
        bal = self._balance(nodo)

        if bal > 1 and clave < nodo.izq.clave:
            return self._rotar_der(nodo)
        if bal < -1 and clave > nodo.der.clave:
            return self._rotar_izq(nodo)
        if bal > 1 and clave > nodo.izq.clave:
            nodo.izq = self._rotar_izq(nodo.izq)
            return self._rotar_der(nodo)
        if bal < -1 and clave < nodo.der.clave:
            nodo.der = self._rotar_der(nodo.der)
            return self._rotar_izq(nodo)
        return nodo

    def insertar(self, cancion):
        self.raiz = self._insertar(self.raiz, cancion)

    def _buscar(self, nodo, titulo):
        if not nodo:
            return None
        titulo = titulo.lower()
        if titulo == nodo.clave:
            return nodo.cancion
        if titulo < nodo.clave:
            return self._buscar(nodo.izq, titulo)
        return self._buscar(nodo.der, titulo)

    def buscar(self, titulo):
        return self._buscar(self.raiz, titulo)

    def _inorder(self, nodo, lista):
        if nodo:
            self._inorder(nodo.izq, lista)
            lista.append(nodo.cancion)
            self._inorder(nodo.der, lista)

    def inorder(self):
        lista = []
        self._inorder(self.raiz, lista)
        return lista

    def altura(self):
        return self._altura(self.raiz)
    