from servicios.catalogo import Catalogo
from modelos.avl import ArbolAVL
from modelos.arbol_general import construir_desde_catalogo, mostrar
from modelos.heap import HeapTop
from modelos.grafo import Grafo

c = Catalogo()
c.cargar_desde_json("datos/canciones.json")

print(f"SoundLink Grupo 14 - {len(c)} canciones cargadas")

# Prueba TP2
print("\nPrueba busqueda secuencial:", c.buscar("Bohemian Rhapsody"))

# Prueba TP3
titulo = c.listar()[0].titulo
print(f"\nPrueba arbol BST buscando '{titulo}':", c.buscar_con_arbol(titulo))

print("\nTop 5 ordenados (inorder TP3):")
for cancion in c.listar_ordenado()[:5]:
    print(f"- {cancion.titulo} - {cancion.artista}")

# Comparativa de tiempos TP2
t_sec, t_bst = c.comparar_estrategias(titulo)
print(f"\nTiempo secuencial: {t_sec:.5f} ms")
print(f"Tiempo arbol: {t_bst:.5f} ms")

# --- NUEVO TP4 - AVL ---
print("\n--- TP4 - AVL (balanceado) ---")
avl = ArbolAVL()
for cancion in c.listar():
    avl.insertar(cancion)
print(f"Buscando '{titulo}' en AVL:", avl.buscar(titulo))
print(f"Altura AVL: {avl.altura()}, canciones en inorder: {len(avl.inorder())}")

# --- NUEVO TP5 - Arbol General ---
print("\n--- TP5 - Arbol General por Genero ---")
raiz = construir_desde_catalogo(c)
mostrar(raiz)

# --- NUEVO TP6 - Heap Top por Rating ---
print("\n--- TP6 - Heap Top 5 por Rating ---")
heap = HeapTop()
for cancion in c.listar():
    heap.agregar(cancion)
for cancion in heap.top(5):
    print(f"- {cancion.titulo} - {cancion.artista} | Rating: {cancion.rating}")

# --- NUEVO TP7 - Grafo Recomendaciones ---
print("\n--- TP7 - Grafo Recomendaciones ---")
grafo = Grafo()
grafo.construir_desde_catalogo(c)
print(f"Si te gusto '{titulo}', te recomendamos:")
for rec in grafo.recomendar(titulo, 3):
    print(f"- {rec.titulo} - {rec.artista} ({rec.genero})")
    print("\n--- TP8 - Recorridos BFS y DFS ---")
print(f"BFS desde '{titulo}':")
for nombre in grafo.bfs(titulo):
    print(f"- {nombre}")

print(f"\nDFS desde '{titulo}':")
for nombre in grafo.dfs(titulo):
    print(f"- {nombre}")
    print("\nAnálisis TP8:")
print("- BFS: usa cola, busca por niveles, sirve para la canción más cercana. O(V+E)")
print("- DFS: usa pila/recursión, explora en profundidad. O(V+E)")

