from Serviceable import Serviceable
from engines.engine import Engine
from batteries.battery import Battery

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self._engine = engine
        self._battery = battery

    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service()