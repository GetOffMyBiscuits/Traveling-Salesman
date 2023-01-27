import datetime


# The truck class to manage our three truck instantiations
# and provides easier updates and future scalability.
# New trucks may be added with ease for future package management scenarios
class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, departure):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departure = departure
        self.time = departure

    # Override
    def __str__(self):
        return f"Capacity: {self.capacity}, " \
               f"Speed: {self.speed}, " \
               f"Load: {self.load}, " \
               f"Packages: {self.packages}, " \
               f"Mileage: {self.mileage}, " \
               f"Address: {self.address}, " \
               f"Departure: {self.departure} "


# Creates the first, second, and third truck and loads in packages manually
# in the future this can be handled heuristically
truck1 = Truck(16, 18, None,
               [1, 13, 14, 15, 16, 19, 20, 30, 34, 37],  # 13, 15, 19, 20, must be delivered together
               0.0, "4001 South 700 East", datetime.timedelta(hours=8))

truck2 = Truck(16, 18, None,
               [2, 3, 9, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39],  # 3, 9, 18, 36, 38 must be on truck2
               0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20)) # #9 correction
truck3 = Truck(16, 18, None,
               [4, 5, 6, 7, 8, 10, 11, 25, 28, 29, 31, 32, 33, 40],  # 6, 25, 28, 32 can't leave before 9:05
               0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
