import json
import os


if os.path.exists("content.txt"):
    os.remove("content.txt")


class PageLinkIterator:
    """    Класс итератора по каждой стране из файла countries.json ищет страницу из википедии.
    На вход принимает путь к файлу json c названиями стран. Записывает в файл пару страна – ссылка.
    Файл content.txt создается в директории проекта. На каждой итерации файл дозаписывается и возвращается.

    """

    def __init__(self, path):
        with open(path) as f:
            json_data = json.load(f)
        self.json_data = json_data
        self.start = 0
        self.stop = len(json_data)

    def __iter__(self):
        return self

    def __next__(self):
        self.country = "_".join(self.json_data[self.start]["name"]["common"].split(" "))
        self.start += 1
        if self.start < self.stop:
            record = "https://en.wikipedia.org/wiki/" + self.country
            if os.path.exists("content.txt"):
                with open("content.txt", "a", encoding="utf-8") as fl:
                    fl.write(record + "\n")
                    country_file = fl
            else:
                with open("content.txt", "w", encoding="utf-8") as fl:
                    fl.write(record + "\n")
                    country_file = fl
        else:
            raise StopIteration
        result = (record, country_file)
        return result


for item in PageLinkIterator("D:\\Netology\\Iter_countries\\countries.json"):
    print(item)



