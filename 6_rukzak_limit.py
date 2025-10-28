import numpy as np

rukzak_max = 102
# rukzak_max = 30
rukzak_data = [
    [3,  5,  9,  10],  # веса 
    [8,  14, 26, 30],# стоимость
    [10, 40, 10,  7]  # макс. кол-во
]

def print_rukzak_table_numpy(weights, item_count, max_item_count, max_value):
    weights = np.array(weights)
    item_count = np.array(item_count)
    max_item_count = np.array(max_item_count)

    # Вычисления
    total_weight_each = weights * item_count
    sum_items = np.sum(item_count)
    sum_max = np.sum(max_item_count)
    total_weight = np.sum(total_weight_each)

    # Таблица как массив
    table = np.array([
        ["Кол-во", *item_count, sum_items],
        ["Макс.кол-во", *max_item_count, sum_max],
        ["Общ. вес", *total_weight_each, total_weight]
    ], dtype=object)

    headers = np.array(["", *[f"Вес {w}" for w in weights], "Сумма"])

    # Расчёт ширины столбцов
    col_widths = [max(len(str(x)) for x in table[:, i]) if i > 0 else 12 for i in range(table.shape[1])]
    col_widths = [max(col_widths[i], len(str(headers[i])) + 2) for i in range(len(headers))]

    def print_row(row):
        for i, val in enumerate(row):
            print(str(val).ljust(col_widths[i]), end="")
        print()

    # Вывод таблицы
    print("\nРезультат упаковки рюкзака:\n")
    print_row(headers)
    print("-" * sum(col_widths))
    for row in table:
        print_row(row)

    print("\nМаксимальная стоимость, которую можно получить:")
    print(total_weight)

def findMax(rukzak_max, weights, values, max_item_count):
    f = [0] * (rukzak_max+1)
    count = [[0] * len(weights) for _ in range(rukzak_max + 1)]  
    for w in range(min(weights), rukzak_max+1):
        for i in range(len(weights)):
            weight = weights[i]
            value = values[i]
            if (w - weight)>=0  and count[w-weight][i] < max_item_count[i] :
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
    max_item_count = rukzak_data[2]
    max_value, item_count = findMax(rukzak_max, weights, values,max_item_count)
    print_rukzak_table_numpy(weights, item_count, max_item_count, max_value)


if __name__ == "__main__":
    main()
