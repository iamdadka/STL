class Car:
    car_count = 0

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        Car.car_count += 1

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is starting.")

    @staticmethod
    def check_speed_limit(speed):
        return speed <= 120

    @classmethod
    def get_car_count(cls):
        return cls.car_count

    def str(self):
        return f"{self.color} {self.brand} {self.model}"

car1 = Car("Toyota", "Camry", "серебристый")

car1.start_engine()

speed_limit = 100
is_within_limit = Car.check_speed_limit(speed_limit)
print(f"Is {speed_limit} km/h within the speed limit? {is_within_limit}")

total_cars = Car.get_car_count()
print(f"Total cars: {total_cars}")

print(car1.str())