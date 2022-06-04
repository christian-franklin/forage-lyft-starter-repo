import engines.capulet_engine
import engines.sternman_engine
import engines.willoughby_engine
import batteries.spindler_battery
import batteries.nubbin_battery
from datetime import date
from car import Car


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        engine = engines.capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = batteries.spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        engine = engines.willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = batteries.spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool) -> Car:
        engine = engines.sternman_engine.SternmanEngine(warning_light_is_on)
        battery = batteries.spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        engine = engines.willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = batteries.nubbin_battery.NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        engine = engines.capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = batteries.nubbin_battery.NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
