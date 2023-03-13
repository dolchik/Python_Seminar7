# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# save_info = open('/Users/olgadrach/Documents/GB/Python/Seminar/Python_Seminar7/save.txt', 'r', encoding='UTF-8')

# Поиск данных по заданному параметру
def print_info(atribut):
    with open('/Users/olgadrach/Documents/GB/Python/Seminar/Python_Seminar7/save.txt', 'r', encoding='UTF-8') as save_info:
        for line in save_info:
            if str(atribut).lower() in str(line).lower():
                print(line)
            # else:
            #     print('Ошибочный ввод')

# Запрос у пользователя атрибута для поиска
def find_atribut():
        atribut = input('Введите инфо для поиска или оставьте пустым для вывода всех данных: ')
        return atribut


# Добавление данных
def import_new_data():
    print('Введите новые данные в формате: Имя Фамилия Телефон')
    with open('/Users/olgadrach/Documents/GB/Python/Seminar/Python_Seminar7/save.txt', 'a', encoding='UTF-8') as save_info:
        save_info.writelines(input('Строка ввода: '))
        save_info.write('\n')
        print('Данные внесены')
# print_info(find_atribut())
import_new_data()