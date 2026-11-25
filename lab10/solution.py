import numpy as np

def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    return np.array(matrix)[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    arr = np.array(matrix).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()

def matrix_vector_product(matrix, vector):
    return (np.array(matrix) @ np.array(vector)).tolist()

def matrix_multiply(left, right):
    return (np.array(left) @ np.array(right)).tolist()

def transpose_matrix(matrix):
    return np.array(matrix).T.tolist()

def solve_system(matrix, vector):
    return np.round(np.linalg.solve(np.array(matrix), np.array(vector)), 6).tolist()

def tensor_channel_mean(tensor):
    return np.array(tensor).mean(axis=-1).tolist()

def point_distance(first, second):
    return round(float(np.linalg.norm(np.array(first) - np.array(second))))