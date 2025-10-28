rukzak_max = 1000001
# rukzak_max = 30
rukzak_data = [
    [3, 5, 9],  
    [8, 14, 26]  
]

def findMax(rukzak_max, weights, values):
    f = [0] * (rukzak_max+1)
    count = [[0] * len(weights) for _ in range(rukzak_max + 1)]  
    for w in range(0, rukzak_max+1):
        for i in range(len(weights)):
            weight = weights[i]
            value = values[i]
            if (w - weight)>=0:
                oldF=f[w]
                f[w] = max(f[w], f[w - weight] + value)
                if (f[w] != oldF):
                    count[w] = count[w - weight][:]  # копируем количество предметов
                    count[w][i] += 1  # увеличиваем количество текущего предмета
    # for i in range(len(f)):
    #     print(i,' = ', f[i])
    return f[rukzak_max], count[rukzak_max]

def main():
    weights = rukzak_data[0]
    values = rukzak_data[1]
    max_value, item_count = findMax(rukzak_max, weights, values)
    print(f"Максимальная стоимость, которую можно получить: {max_value}")
    print("Состав рюкзака:")
    for i in range(len(weights)):
        print(f"Вес {weights[i]}: {item_count[i]}")
if __name__ == "__main__":
    main()
