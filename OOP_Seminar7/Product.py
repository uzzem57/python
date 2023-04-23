from abc import abstractclassmethod, abstractmethod

class Product:
    volume = 0
    name =""

    def __init__(self, name, volume) -> None:
        self.name = name
        self.volume = volume


    def getName(self):
        return self.name
    def getVolume(self):
        return self.volume
    def setName(self,name):
        self.name = name

    def setVolume(self,volume):
        self.volume = volume

