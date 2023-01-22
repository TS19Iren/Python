import model
def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['Показать все контакты',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Найти контакт',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = input('Введи команду >: ')
    while not user_input.isdigit() or int(user_input) > len(menu_list) or int(user_input) <= 0:
        user_input = input('Введи команду >: ')
    return int(user_input)


def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()

def delete_contact():
    show_all(model.db_list)
    id_contact_to_del = int(input('Введите номер удаляемого контакта: '))
    model.db_list.pop(id_contact_to_del-1)
    show_all(model.db_list)

def db_success(db: list):
    if db:
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы.')
    exit()


def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()

    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = input('\tВведите телефон >: ')
    new_contact['comment'] = input('\tВведите комментарий >: ')
    return new_contact

def change_contact():
    show_all(model.db_list)
    id_contact_to_change = int(input('Введите номер изменяемого контакта: '))
    change = int(input('Чтобы изменить фамилию, нажмите - 1, имя - 2, телефон - 3, комментарий - 4. Что будем менять? '))
    while change<0 or change>4:
        change = int(
            input('Укажите номер изменяемого параметра: фамилия - 1, имя - 2, телефон - 3, комментарий - 4. Что будем менять? '))
    changed_info = input('Укажите измененные данные: ')
    contact_to_change = find_contact_by_index(id_contact_to_change-1, model.db_list)
    match change:
        case 1:
            contact_to_change['lastname'] = changed_info
        case 2:
            contact_to_change['firstname'] = changed_info
        case 3:
            contact_to_change['phone'] = changed_info
        case 4:
            contact_to_change['comment'] = changed_info
    show_all(model.db_list)
    model.write_db_file()
def find_contact_by_index(index: int, db: list):
    return db[index]

def find_contact(db: list):
    value = input('Введите текст: ')
    result = []
    for i in db:
        if value == i['phone']:
            result.append(i)
            continue
        if value == i['lastname']:
            result.append(i)
            continue
        if value == i['firstname']:
            result.append(i)
    print(f'Найден контакт: {result}')
