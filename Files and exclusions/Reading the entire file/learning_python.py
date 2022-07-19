filename = 'learning_python.txt'
with open(filename) as python_notes:
    notes_all = python_notes.read()


class ReadFile:
    """Инициализирует атрибут notes"""

    def __init__(self, notes):
        self.notes = notes

    def read_all(self):
        print(self.notes)

    @staticmethod
    def read_all_by_lines():
        with open(filename) as python_lines:
            for line in python_lines:
                print(line)


notes_1 = ReadFile(notes_all)
notes_1.read_all()

notes_2 = ReadFile(notes_all)
notes_2.read_all_by_lines()
