filename = 'learning_python.txt'
with open(filename) as python_notes:
    notes_all = python_notes.read()


class ReadFile:
    """Инициализирует атрибут notes"""

    def __init__(self, notes):
        self.notes = notes

    def read_all(self):
        print(f"--- Чтение всего содержимого файла: \n{self.notes}")

    @staticmethod
    def read_all_by_lines():
        print("\n--- Чтение с перебором строк объекта файла: ")
        with open(filename) as python_lines:
            for line in python_lines:
                print(line.rstrip())

    @staticmethod
    def lines_in_list():
        print("\n--- Сохранение строк в списке:")
        with open(filename) as python_list:
            lines = python_list.readlines()
        for string in lines:
            print(string.rstrip())

    @staticmethod
    def replace_word():
        print("\n--- Изменение Python на C#:")
        replace_notes = notes_all.replace('Python', 'C#')
        print(replace_notes)


notes_1 = ReadFile(notes_all)
notes_1.read_all()

notes_2 = ReadFile(notes_all)
notes_2.read_all_by_lines()

notes_3 = ReadFile(notes_all)
notes_3.lines_in_list()

notes_4 = ReadFile(notes_all)
notes_4.replace_word()
