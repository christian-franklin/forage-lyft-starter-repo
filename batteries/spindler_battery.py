from datetime import datetime
from batteries.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self._last_service_date = last_service_date
        self._current_date = current_date

    def needs_service(self):
        """
        Updated from 2 to 3 years.
        """
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 3)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
