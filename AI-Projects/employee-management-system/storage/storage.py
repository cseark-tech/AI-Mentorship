from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def save(self, employees):
        pass

    @abstractmethod
    def load(self):
        pass