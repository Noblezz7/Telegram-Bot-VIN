#Импортируем библиотеки
import pymongo
from colors import colors
from vininfo import Vin

class DB:
    def __init__(self):
        #Создаём соединение с монго при инициализации объекта класса
        self.conn = pymongo.MongoClient('localhost', 27017)

    def assembleResult(self, responseString, crashes):
        for crash in crashes:
            responseString += "- " + crash + "\n"
        return responseString

    def getCarByVIN(self, vinNumber):
        responseHeader = "VIN: " + vinNumber + "\n" + "Аварии:\n"
        queryResult = self.conn.cars.cars.find_one({"VIN": vinNumber})
        if(queryResult):
            if(len(queryResult["crashes"]) == 0):
                return False
            else:
                return self.assembleResult(responseHeader, queryResult["crashes"])
        else:
            return False