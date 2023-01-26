import controller
# def main_menu(students: list):
#     menu = "Выберите предмет:"
#     print(menu)
#     list_lessons = []
#     for i in student_base:
#         for les in i.lessons:
#             list_lessons.append(les.name)
#     set_lessons = set(list_lessons)
#     for number, lessons in enumerate(set_lessons, 1):
#         print(number, lessons)
#     user_input = input('Введите номер предмета: ')
#     while not user_input.isdigit() or int(user_input)<0 or int(user_input)==0 or int(user_input)>len(set_lessons):
#         user_input = input('Введите номер предмета: ')
#     return int(user_input)

def start_menu():
    subjects = controller.first_menu()

    while True:
        show_numerated_list(subjects)
        user_input = controller.ask_user_valid('Введите значение:', subjects)
        user_sub_choice = subjects[user_input-1]
        list_students = controller.show_students(user_sub_choice)
        show_numerated_list(list_students)

        user_input = controller.ask_user_valid('Кто пойдет к доске?', list_students)
        student_mark = controller.valid_mark('Какую оценку постаивть студенту?')
        controller.set_mark(list_students[user_input-1], user_sub_choice, student_mark)



def show_numerated_list(my_list: list):
    for index, elem in enumerate(my_list, 1):
        print(index, elem)
    print('Введите 0 для выхода')


