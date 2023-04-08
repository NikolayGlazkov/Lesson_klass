def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        row = ""
        for j in range(1, num_columns+1):
            element = str(operation(i, j)).rjust(2) # получаем элемент с помощью переданной функции и преобразуем его в строку
            row += element + " " # добавляем элемент в строку для текущей строки
        print(row) # выводим строку

# Пример использования:
print_operation_table(lambda x, y: x * y)



#данный код написан не мной, я не понял задание