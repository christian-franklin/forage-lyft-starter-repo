from tires.tire import Tire


class Octoprime(Tire):
    def __init__(self, sensors):
        self._sensors = sensors

    def needs_service(self):
        total = 0
        for i in self._sensors:
            total += i
            if total >= 3:
                return True
        return False
