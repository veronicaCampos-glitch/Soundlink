class Cancion:
    def __init__(self, titulo, artista, genero, anio, rating, cols=None):
        self.titulo=titulo; self.artista=artista; self.genero=genero; self.anio=anio; self.rating=rating; self.colaboraciones=cols or []
    def __repr__(self): return f"{self.titulo} - {self.artista} ({self.genero})"
