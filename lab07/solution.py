import numpy as np


def reshape_rows(values, width):
    if width <= 0:
        return []
    if len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return []
    return arr.reshape(-1, width).tolist()


def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0 or len(rows) == 0 or len(columns) == 0:
        return []
    result = arr[np.ix_(rows, columns)]
    return result.tolist()


def column_means(matrix):
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return []
    means = arr.mean(axis=0)
    return [round(float(x), 6) for x in means]


def column_range(matrix, column):
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return 0.0
    col = arr[:, column]
    return 0 