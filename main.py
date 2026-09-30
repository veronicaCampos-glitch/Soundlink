from servicios.catalogo import Catalogo

c = Catalogo()
c.cargar_desde_json("datos/canciones.json")

print(f"SoundLink Grupo 14 - {len(c)} canciones cargadas")

# Prueba TP2
print("\nPrueba busqueda secuencial:", c.buscar("love"))

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
