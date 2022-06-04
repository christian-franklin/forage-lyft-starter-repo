from abc import ABC, abstractmethod
from Serviceable import Serviceable


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass

    