import json
from modelos.cancion import Cancion
class Recomendador:
    def __init__(self): self.canciones=[]
    def cargar_datos(self):
        import json
        f=open("datos/canciones.json",encoding="utf-8"); datos=json.load(f)
        self.canciones=[Cancion(d["titulo"],d["artista"],d["genero"],d["anio"],d["rating"],d["colaboraciones"]) for d in datos]
    def buscar(self,t):
        for c in self.canciones:
            if t.lower() in c.titulo.lower(): return c
    def top(self,n=10): return sorted(self.canciones,key=lambda x:x.rating,reverse=True)[:n]
