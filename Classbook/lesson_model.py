class Lesson:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks



    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_mark(self):
        return self.marks

    def set_marks(self, marks):
        self.marks = marks

# метод добавления одной оценки
    def add_mark(self, mark: int):
        self.marks.append(mark)