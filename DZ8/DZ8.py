# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def menu():
    print(' ')
    choice = int(input('Выберите взаимодействие с телефонным справочником: \n1 - Вывести данные справочника \n2 - Найти информацию в справочнике \n3 - Записать новые данные \n4 - Изменть данные \n5 - Удалить данные \n6 - Выйти \nВведите цифру (от 1 до 6): '))
    print(' ')
    return choice

def print_list(file_list):
    print('Данные из справочника: ')
    for i in range(len(file_list)):
        print(f'{i+1}. {file_list[i].strip()}')
    print(' ')

def write_file(file_name, list_):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(list_)

def open_file(file_name):
    file_lines = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for lines in file:
            file_lines.append(lines)
    return(file_lines)

def elem_search(search_name, file_list):
    found_info = []
    for elem in file_list:
        elem = elem.split()
        flag = True
        for _ in range(len(elem)):
            if search_name in elem and flag == True:
                elem = ' '.join(elem)
                found_info.append(elem + ' \n')
                flag = False
    if found_info == []:
        print(' ')
        print('Таких данных нет в справочнике')
    else:
        print(' ')
        print('Найдено в справочнике: ')
        print(*found_info)
    return found_info

def file_search(file_list):
    print('По какой информации вы ищете? \n1 - фамилия \n2 - имя \n3 - отчество \n4 - телефон?')
    search_item = int(input('Введите цифру от 1 до 4: '))
    found_info = []
    if search_item == 1:
        fam = input('Введите фамилию: ')
        found_info = elem_search(fam, file_list)
    elif search_item == 2:
        name_ = input('Введите имя: ')
        found_info = elem_search(name_, file_list)
    elif search_item == 3:
        sername = input('Введите отчество: ')
        found_info = elem_search(sername, file_list)
    else:
        phone_number = input('Введите номер телефона: ')
        found_info = elem_search(phone_number, file_list)
    return found_info

def add_to_phonebook_list(file_list):
    phone_number = input('Введите номер телефона: ')
    lastname = input('Введите фамилию с заглавной буквы: ')
    name_ = input('Введите имя с заглавной буквы: ')
    sername = input('Введите отчество с заглавной буквы: ')
    pesrson_info = phone_number + ' ' + lastname + ' ' + name_ + ' ' + sername + ' \n'
    file_list.append(pesrson_info)
    return file_list

def change_data(file_list, found_data):
    choice = int(input('Вы хотите изменить найденные данные? \n1 - Да \n2 - Нет \nВведите (1 или 2):'))
    print(' ')
    if choice == 1:
        if len(found_data) > 1:
            choice2 = int(input('Вы хотите изменить все найденные данные? \n1 - Все данные \n2 - Только одну запись \nВведите 1 или 2: '))
            if choice2 == 1:
                for i in range(len(found_data)):
                    file_list.remove(found_data[i])
                    file_list.append(input('Введите новые данные (Тел ФИО): ') + ' \n')
                return file_list
            elif choice2 == 2:
                choice3 = int(input('Какую запись вы хотите изменить? \nВведите порядковый номер записи(нумерация начинается с 1): '))
                for i in range(len(found_data)):
                    if i+1 == choice3:
                        file_list.remove(found_data[i])
                        file_list.append(input('Введите новые данные (Тел ФИО): ') + ' \n')
                return file_list
        else:
            for i in range(len(found_data)):
                file_list.remove(found_data[i])
                file_list.append(input('Введите новые данные (Тел ФИО): ') + ' \n')
            return file_list
    elif choice == 2:
        return file_list

def confirm_for_change(file_name, changed_list):
    choice = int(input('Подверждаете изменения? \n1 - Да \n2 - Нет \nВведите 1 или 2: '))
    if choice == 1:
        write_file(file_name, changed_list)
    else:
        return False

def confirm_for_add(file_name, changed_list):
    choice = int(input('Подверждаете изменения? \n1 - Да \n2 - Нет \nВведите 1 или 2: '))
    if choice == 1:
        write_file(file_name, changed_list)
    else:
        return False


def delete_data(file_list, found_data):
    choice = int(input('Вы хотите УДАЛИТЬ найденные данные? \n1 - Да \n2 - Нет \nВведите (1 или 2):'))
    print(' ')
    if choice == 1:
        if len(found_data) > 1:
            choice2 = int(input('Вы хотите УДАЛИТЬ все найденные данные? \n1 - Все данные \n2 - Только одну запись \nВведите 1 или 2: '))
            if choice2 == 1:
                for i in range(len(found_data)):
                    file_list.remove(found_data[i])
                return file_list
            elif choice2 == 2:
                choice3 = int(input('Какую запись вы хотите УДАЛИТЬ? \nВведите порядковый номер записи(нумерация начинается с 1): '))
                for i in range(len(found_data)):
                    if i+1 == choice3:
                        file_list.remove(found_data[i])
                return file_list
        else:
            for i in range(len(found_data)):
                file_list.remove(found_data[i])
            return file_list
    elif choice == 2:
        return file_list

def main():
    choice = menu()
    if choice == 1:
        ph_book = open_file('ph_book.txt')
        print_list(ph_book)
        main()
    elif choice == 2:
        ph_book = open_file('ph_book.txt')
        file_search(ph_book)
        main()
    elif choice == 3:
        ph_book = open_file('ph_book.txt')
        ph_book_extend = add_to_phonebook_list(ph_book)
        print(' ')
        print_list(ph_book_extend)
        confirm_for_add('ph_book.txt', ph_book_extend)
        main()
    elif choice == 4:
        ph_book = open_file('ph_book.txt')
        found_data = file_search(ph_book)
        changed_book = change_data(ph_book, found_data)
        print(' ')
        print_list(changed_book)
        confirm_for_change('ph_book.txt', changed_book)
        main()
    elif choice == 5:
        ph_book = open_file('ph_book.txt')
        found_data = file_search(ph_book)
        ph_book_reduce = delete_data(ph_book, found_data)
        print(' ')
        print_list(ph_book_reduce)
        confirm_for_add('ph_book.txt', ph_book_reduce)
        main()
    elif choice == 6:
        print('Вы закончили работу со справочником')
    else:
        print('Вы ввели некорректное значение')
        main()

if __name__== '__main__':
    main()
