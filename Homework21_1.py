class FileContextManager:
    counter = 0

    def __init__(self, filepath, mode):
        self.filepath = filepath
        self.mode = mode
        self.file = None

    def __enter__(self):
        FileContextManager.counter += 1
        self.file = open(self.filepath, self.mode)
        print(f"Файл '{self.filepath}' открыт. Количество использований: {FileContextManager.counter}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"Файл '{self.filepath}' закрыт.")

        if exc_type:
            print(f"Произошло исключение: {exc_type.__name__} - {exc_value}")
            return False

        return True


# Пример использования
if __name__ == "__main__":
    try:
        with FileContextManager("example.txt", "w") as f:
            f.write("Hello world")

        # Проверяем счетчик
        print(f"Количество использований файла: {FileContextManager.counter}")
    except Exception as e:
        print(f"Ошибка: {e}")
