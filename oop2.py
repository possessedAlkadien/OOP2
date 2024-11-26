import os
import time

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
            return 0

    def xmlFile(self,file):
        XMLdata = []
        content = file.read()
        content = content.replace("\n", "").replace("\r", "")
        count = 1
        while "<" in content:
            if count>2:
                start = content.index("<") + len("<")
                end = content.index("/>")
                entry_block = content[start:end]

                city = content.split('city="')[1].split('"')[0]
                street = content.split('street="')[1].split('"')[0]
                house = content.split('house="')[1].split('"')[0]
                floors = content.split('floor="')[1].split('"')[0]

                XMLdata.append((city, street, house, floors))
                content = content[end + len("/>"):]
            count+=1
        return XMLdata

    def csvFile(self,file):
        CSVdata = []
        count = 0
        for line in file:
            line = line.strip()
            line = line.replace('"','')
            count+=1
            if line and count!=1:
                city,street,house,floors = line.split(";")
                CSVdata.append((city.strip(), street.strip(), house.strip(), floors.strip()))
        return CSVdata

class Statistics:
    def duplicateEntries(self,Sdata):
        print("Дубликаты в списке:")
        counter = {}
        for address in Sdata:
            counter[address] = counter.get(address,0)+1
        duplicates = {dupl: count for dupl,count in counter.items() if count>1}
        print(duplicates)
        print("\n")

    def floorsCounter(self,Fdata):
        print("Количество этажей в городах: \n")
        counter = {}
        for address in Fdata:
            counter[address[3]] = counter.get(address[3],0)+1
        duplicates = {dupl: count for dupl,count in counter.items()}
        duplicates = sorted(duplicates.items(), key=lambda item: item[0])
        print(duplicates)
        print("\n")



def main():
    ExitFlag = False
    while (ExitFlag != True):
        userFile = File()
        path = userFile.findFile(userFile.filePath())
        if path == '0':
            ExitFlag = True
            print("Закрытие программы...")
        elif path != 0:
            file = open(path)
            analysis = Statistics()
            if '.xml' in path:
                data = userFile.xmlFile(file)
            elif '.csv' in path:
                data = userFile.csvFile(file)
            else:
                print("Формат файла не поддерживается.")
                print("\n")

            startTime = time.time()
            if data:
                analysis.duplicateEntries(data)
                analysis.floorsCounter(data)
            endTime = time.time()
            print("Время обработки файла", endTime-startTime)
            print("\n")


if __name__ == '__main__':
    main()