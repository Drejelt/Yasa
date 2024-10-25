def count_lines(name):
    try:
        with open(name, encoding='utf-8') as file: #Спасибо гуглу, ибо у меня были проблемы и без encoding='utf-8' ничего не работало.
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return f"Файл '{name}' не найден."


def count_chars(name):
    try:
        with open(name, encoding='utf-8') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        return f"Файл '{name}' не найден."


def test(name):
    line_count = count_lines(name)
    char_count = count_chars(name)

    print(f"Файл: {name}")
    print(f"Количество строк: {line_count}")
    print(f"Количество символов: {char_count}")