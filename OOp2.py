import os

class File:
    def filePath(self):
        path = str(input("Введите путь к файлу:"))
        return path
    def readFile(self, path):
        if os.path.exists(path):
            file = open(path)
            for row in file:
                print(row)
        else:
            print("Произошла ошибка в чтении файла.")


def main():
    userFile = File()
    userFile.readFile(userFile.filePath())

if __name__ == '__main__':
    main()
