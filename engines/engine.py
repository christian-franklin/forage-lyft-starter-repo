from abc import ABC, abstractmethod
from Serviceable import Serviceable


class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass
