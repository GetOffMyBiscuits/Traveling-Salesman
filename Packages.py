# Packages class, provides an easy way to manage packages
# and improves scalability by providing a simple way to
# add, update, delete new or existing packages.
class Packages:
    def __init__(self, pid, address, city, state, postal, deadline, weight, status):
        self.pid = pid
        self.address = address
        self.city = city
        self.state = state
        self.postal = postal
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery = 0
        self.departure = 0

    # Override
    def __str__(self):
        return f"{self.pid}, " \
               f"{self.address}, " \
               f"{self.city}, " \
               f"{self.state}, " \
               f"{self.postal}, " \
               f"deadline: {self.deadline}, " \
               f"delivered: {self.delivery}, " \
               f"{self.weight}, " \
               f"status: {self.status} "

    # Function to set the trucks status depending on the point in time
    def set_status(self, input_time):
        if self.delivery < input_time:
            self.status = "delivered"
        elif self.departure > input_time:
            self.status = "en route"
        else:
            self.status = "At the hub"
