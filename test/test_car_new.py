import unittest
from datetime import datetime
from car_factory import CarFactory

"""
Replaced old tests from test_car with below. 
"""

class TestCalliope(unittest.TestCase):
    """
    Updated to reflect change in spindler battery (threshold increased from 2 to 3 years).
    Updated to test tire_wear.
    """
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0.3, 1.2, 0.3, 0.4]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

class TestGlissade(unittest.TestCase):
    """
    Updated to reflect change in spindler battery.
    Updated to test tire_wear.
    """
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 1, 2, 1]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

class TestPalindrome(unittest.TestCase):
    """
    Updated to reflect change in spindler battery.
    """
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire_wear = [0.1, 1.2, 0.3, 0.1]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())

class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear = [0, 1, 3, 1]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear = [0, 1, 0, 1]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0.1, 1.2, 0.3, 0.1]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0.1, 0.2, 0.3, 0.1]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
