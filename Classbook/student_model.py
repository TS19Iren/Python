import lesson_model


class Student:
    def __init__(self, name: str, lessons: list):
        self.name = name
        self.lessons = lessons

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_lessons(self):
        return self.lessons

    def set_lessons(self, lessons):
        self.lessons = lessons
