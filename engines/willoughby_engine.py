from engines.engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    def needs_service(self):
        return self._current_mileage - self._last_service_mileage > 60000
