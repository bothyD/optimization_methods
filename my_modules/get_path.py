# Функция восстановления пути
def get_path(prev, t):
    path = []
    while t is not None:
        path.append(t)
        t = prev[t]
    path.reverse()
    return path