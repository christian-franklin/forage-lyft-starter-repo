from tires.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensors):
        self._sensors = sensors

    def needs_service(self):
        for i in self._sensors:
            if i >= 0.9:
                return True
        return False
