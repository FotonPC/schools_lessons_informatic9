import numpy as np

height_matrix = int(input("Сколько строк:"))
width_matrix = int(input("Сколько столбцов:"))

my_matrix = [list(map(float, input().split())) for i in range(height_matrix)]  # ВВОД матрицы


def my_transpose(in_matrix, width_of_matrix, height_of_matrix):
    result = np.zeros((width_of_matrix, height_of_matrix))
    for i in range(width_of_matrix):
        for j in range(height_of_matrix):
            result[i][j] = in_matrix[j][i]
    return result


def formating_number(number, length):
    len2 = len(str(number))
    return str(number) + ' ' * (length - len2)


def matrix_to_string(matrix, width_of_matrix, height_of_matrix):
    maximal_length = len(str(np.max(matrix)))  # Максимальный элемент для форматирования
    output = ''
    for i in range(height_of_matrix):
        # Формируем линию
        output += "+" + ("-" * (maximal_length + 1) + '-+') * width_of_matrix + '\n'
        output += '| '
        for j in range(width_of_matrix):
            # Добавляем 1 число
            output += formating_number(matrix[i][j], maximal_length) + ' | '
        output += '\n'
    # Последняя линия
    output += "+" + ("-" * (maximal_length + 1) + '-+') * width_of_matrix
    return output


print(matrix_to_string(my_transpose(np.array(my_matrix), width_matrix, height_matrix), width_matrix, height_matrix))
