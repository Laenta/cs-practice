def count_items(values):
    counts = {}
    for i in values:
        counts[i] = counts.get(i, 0) + 1
    return counts


def unique_sorted(values):
    return sorted(set(values))


def common(first, second):
    return sorted(set(first) & set(second))


def only_in_first(first, second):
    return sorted(set(first) - set(second))

values = ["ошибка", "запуск", "ошибка", "проверка"]

print(count_items(values)  )  # {"ошибка": 2, "запуск": 1, "проверка": 1}
print(unique_sorted(values))  # ["запуск", "ошибка", "проверка"]

print(common(["иванов", "петрова"], ["петрова", "котов"])  )      # ["петрова"]
print(only_in_first(["иванов", "петрова"], ["петрова", "котов"])) # ["иванов"]