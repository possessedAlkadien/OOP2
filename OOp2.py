import os

data = []

class File:
    def filePath(self):
        print("Для выхода введите 0.")
        path = str(input("Введите путь к файлу:"))
        return path

    def findFile(self, path):
        if path == '0':
            return path
        if os.path.exists(path):
            return path
        else:
            print("Произошла ошибка! Такого файла не существует.")

    def xmlFile(self,file):
        print("q")

    def csvFile(self,file):
        print("q")


def main():
    ExitFlag = False
    while (ExitFlag != True):
        userFile = File()
        path = userFile.findFile(userFile.filePath())
        if path == '0':
            ExitFlag = True
            print("Закрытие программы...")
        else:
            file = open(path)
            if '.xml' in path:
                userFile.xmlFile(file)
            elif '.csv' in path:
                userFile.csvFile(file)
            else:
                print("Формат файла не поддерживается.")

if __name__ == '__main__':
    main()
