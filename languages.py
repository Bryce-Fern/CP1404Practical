from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    language = [ruby, python, visual_basic]
    print("The dynamically typed languages are: ")
    for dynamic in language:
        if dynamic.is_dynamic():
            print(dynamic.name)


main()
