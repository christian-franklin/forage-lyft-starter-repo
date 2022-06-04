from Serviceable import Serviceable
from engines.engine import Engine
from batteries.battery import Battery
from tires.tire import Tire

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self._engine = engine
        self._battery = battery
        self._tire = tire

    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service() or self._tire.needs_service()
