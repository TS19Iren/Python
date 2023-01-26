import json
import view
import student_model
import lesson_model
from collections import namedtuple


def read_file(file: str):
    file_name = file
    try:
        with open(file_name, 'r', encoding='utf-8') as data_file:
            return json.load(data_file, object_hook=student_decoder)

    except:
        print('Файл не существует')

def write_file(file: str,student_base):
    student_base = list_to_students(student_base)
    with open(file, 'w', encoding='utf-8') as data_file:
        json.dump(student_base,data_file,default=lambda o: o.__dict__, indent=4, ensure_ascii=False)
def list_to_students(list_of_students: list):
    students = []
    for st in list_of_students:
        lessons = []
        for les in st.lessons:
            lessons.append(lesson_model.Lesson(les.name, les.marks))
        students.append(student_model.Student(st.name, lessons))
    return students
def ask_user_valid(question: str,list: list):
    user_input = input(question)

    while not user_input.isdigit() or int(user_input)<0 or int(user_input)>len(list):
        user_input = input((question))
    user_answer = int(user_input)
    if user_answer==0:
        exit(0)
    return user_answer



def valid_mark(question: str):
    mark = input(question)
    while not mark.isdigit() or int(mark)<0 or int(mark)>5:
        mark = input(question)
    return int(mark)

def student_decoder(dictionary: dict):
    return namedtuple('X', dictionary.keys())(*dictionary.values())

def first_menu()->list:
    global student_base
    student_base = read_file("data.json")
    return show_subjects()


def show_subjects():
    list_lessons = []
    for i in student_base:
        for les in i.lessons:
            list_lessons.append(les.name)
    return list(set(list_lessons))

def set_mark(student_name_witth_marks: str, lesson, mark):
    global student_base
    st_name = student_name_witth_marks.split(',')[0]
    for st in student_base:
        if st.name == st_name:
            for les in st.lessons:
                if les.name == lesson:
                    les.marks.append(mark)
    write_file('data.json',student_base)

def show_students(lesson_name):
    global student_base
    list_students = []
    for st in student_base:
        for les in st.lessons:
            if les.name == lesson_name:
                list_students.append(f'{st.name}, оценки {les.marks}')
    return list_students


