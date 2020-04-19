class ProgrammingLanguage:

    def __init__(self, year, reflection, typing, name):
        self.year = year
        self.name = name
        self.reflection = reflection
        self.typing = typing

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"
