class Graph:
    def __init__(self, filePath: str) -> None:
        # decidir a estrutura de dados da implementação (matriz, hash table...)
        ...

    def qtdVertices(self) -> int:
        ...

    def qtdArestas(self) -> int:
        ...

    # TODO: `tipodovertice` a definir
    def grau(self, vertice: tipodovertice) -> int:
        ...

    def rotulo(self, vertice: tipodovertice) -> str:
        ...

    def vizinhos(self, vertice: tipodovertice) -> list[tipodovertice]:
        ...

    def peso(self, v1: tipodovertice, v2: tipodovertice) -> int:
        ...
