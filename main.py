from servicios.recomendador import Recomendador
r=Recomendador(); r.cargar_datos()
print(f"SoundLink Grupo 14 - {len(r.canciones)} canciones cargadas")
print("Top:", r.top(3))
