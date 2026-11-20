# SoundLink - Grupo 14
Fernandez Axel 46815105 - Campos Veronica 27382376 - Comision 2 - Prof Zorzoli
Dominio Musica

## ¿De qué se trata el proyecto?

Soundlink es una aplicación de música tipo Spotify.

La idea es simple: cargás canciones y la app te recomienda canciones parecidas a la que te gusta.

## ¿Por qué elegimos este proyecto?

Porque queríamos hacer algo real, que se use de verdad, no solo números. Si te gusta Queen, tiene sentido que te recomiende otra canción de Rock.

## ¿Qué estructuras usamos y por qué?

- **Árbol AVL:** para buscar canciones por título muy rápido, manteniendo el árbol balanceado.
- **Árbol General:** para organizar las canciones por género, como carpetas: Rock, Pop, etc.
- **Heap:** para armar el Top 5 de las canciones más escuchadas.
- **Grafo:** para conectar canciones que tienen el mismo género o el mismo artista.
- **BFS y DFS:** para recorrer el grafo y buscar recomendaciones. BFS busca por niveles, DFS explora en profundidad.

## ¿Cómo se ejecuta?

```bash
python main.py