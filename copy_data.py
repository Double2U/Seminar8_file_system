from return_data_file import data_file

def copy_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пустой!")
    else:
        number_row = int(input(f"Введите номер строки, которую необходимо скопировать: "
                               f"от 1 до {count_rows}: "))
    while number_row < 1 and number_row > count_rows:           
        number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
    data_row = data[number_row - 1]
    number = int(input("Выберите файл, куда необходимо вставить строку:  "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    with open(f'db/data_{number}.txt', 'a', encoding='utf-8') as file:
        file.write(data_row)
    print("Данные скопированы и вставлены!") 