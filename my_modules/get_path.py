# Функция восстановления пути
def get_path(prev: list, t: int) -> list:
    path = []
    while t is not None:
        path.append(t)
        t = prev[t]
    path.reverse()
    return path