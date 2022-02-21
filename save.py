import json
import os
import stat

FILE: str = "Save.json"

_startData_v02: dict = {
    "visits": 0,
    "prefix": "> ",
    "money": 1000,
    "delete_/": False
}


class Save:

    def checkSave(self, data: dict) -> dict:
        if data.keys() != _startData_v02:
            data_return: dict = _startData_v02

            for i in data:
                data_return[i] = data[i]
            return data_return

        return data


    def getSave(self) -> dict:
        """
        Считываем данные из файла в переменную

        :return: (dict) Данные файла
        """
        try:
            os.chmod(FILE, stat.S_IRUSR | stat.S_IROTH | stat.S_IWUSR | stat.S_IXUSR)
            with open(FILE, "r") as fl:
                data = self.checkSave(json.load(fl))
                os.chmod(FILE, stat.S_IROTH)

        except:
            with open(FILE, "w") as fl:
                data = _startData_v02
                self.doSave(data)
                os.chmod(FILE, stat.S_IROTH)
        return data


    def doSave(self, data: dict) -> None:
        """
        Записывает сохранения в файл

        :param data: то, что сохраняем
        """
        try:
            os.chmod(FILE, stat.S_IRUSR | stat.S_IROTH | stat.S_IWUSR | stat.S_IXUSR)
            with open(FILE, "w") as fl:
                json.dump(data, fl, indent=2)
                os.chmod(FILE, stat.S_IROTH)

        except:
            print("\n\n:[Не удалось сохранить данные]\n\n")
            input("/")








