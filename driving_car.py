import random
import configfile

car_fleet: list = []
car_to_remove: list = []


class NotEnoughFuel(Exception):
    pass


def generate_random_color():
    # Generating a random color in HEX format
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"


class Car:
    mileage: int
    fuel: int
    economy: float
    color: str
    model: str

    def __init__(
        self,
        economy,
        color,
        model,
        mileage=configfile.DEFAULT_MILEAGE,
        fuel=configfile.DEFAULT_FUEL,
    ):
        self.__mileage = mileage
        self.__fuel = fuel
        self.__economy = economy
        self.__color = color
        self.__model = model

    @property
    def get_fuel_value(self):
        return self.__fuel

    def drive(self, distance) -> None:
        if self.__fuel - (distance / 100) * self.__economy < 0:
            raise NotEnoughFuel(
                f"\nNot enough fuel to cover the distance {distance} miles. Fuel left for"
                f" {round(self.distance_left(), configfile.SYMBOLS_AFTER_COMMA)} miles"
            )
        else:
            self.__mileage += distance
            self.__fuel = self.__fuel - (distance / 100) * self.__economy

    def distance_left(self) -> float:
        return (self.__fuel / self.__economy) * 100

    def fuel_up(self) -> None:
        self.__fuel += configfile.FUEL_UP_VALUE

    def show_info(self):
        print(
            f"Mileage: {self.__mileage}, Fuel: {round(self.__fuel, configfile.SYMBOLS_AFTER_COMMA)}, Economy:"
            f" {round(self.__economy, configfile.SYMBOLS_AFTER_COMMA)}, Color: {self.__color}, Model: {self.__model}"
        )


def drive_distance(distance: int):
    for car in car_fleet:
        try:
            car.drive(distance)
        except NotEnoughFuel as error:
            print(error)
            print("A car with an almost empty tank will be excluded from the fleet:")
            car.show_info()
            car_to_remove.append(car)


def delete_cars_from_fleet():
    for car in car_to_remove:
        car_fleet.remove(car)
    car_to_remove.clear()


def show_car_fleet():
    for car in car_fleet:
        car.show_info()


def fuel_up_fleet():
    for car in car_fleet:
        car.fuel_up()


def car_with_largest_remaining_fuel():
    if len(car_fleet):
        car_most_residual_fuel = max(
            car_fleet, key=lambda car: car.get_fuel_value, default=None
        )
        print("\nCar with the largest residual fuel:")
        car_most_residual_fuel.show_info()
        print(
            f"Fuel left for {round(car_most_residual_fuel.distance_left(), configfile.SYMBOLS_AFTER_COMMA)} miles"
        )
    else:
        print("No cars left.")


def car_fleet_creating():
    for _ in range(configfile.CARS_IN_FLEET):
        car_fleet.append(
            Car(
                mileage=configfile.DEFAULT_MILEAGE,
                fuel=configfile.DEFAULT_FUEL,
                economy=random.uniform(configfile.MIN_ECONOMY, configfile.MAX_ECONOMY),
                color=generate_random_color(),
                model=random.choice(configfile.models),
            )
        )


car_fleet_creating()
print("Car park before travel and refueling:")
show_car_fleet()
drive_distance(configfile.FIRST_DISTANCE)
delete_cars_from_fleet()
fuel_up_fleet()
drive_distance(configfile.SECOND_DISTANCE)
delete_cars_from_fleet()
print("\nCar park after travel and refueling:")
show_car_fleet()
car_with_largest_remaining_fuel()
