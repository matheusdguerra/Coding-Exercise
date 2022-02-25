# Torre de Hanói
def hanoi(disco: int, origem: str, auxiliar: str, destino: str) -> None:
    if disco <= 0:
        return
    hanoi(disco - 1, origem, destino, auxiliar)
    print(f'Movendo disco {disco} de {origem} para {destino}')
    hanoi(disco - 1, auxiliar, origem, destino)


if __name__ == "__main__":
    hanoi(3, 'Origem', 'Auxiliar', 'Destino')
