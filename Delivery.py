import datetime
import csv
from HashMap import package_hash

# Provides a connection to the Distance CSV file to be read
with open("CSV_Distance.csv") as csv_dist:
    csv_distance = csv.reader(csv_dist)
    csv_distance = list(csv_distance)

# Provides a connection to the Address CSV file to be read
with open("CSV_Address.csv") as csv_locations:
    csv_address = csv.reader(csv_locations)
    csv_address = list(csv_address)


# to find the distance of two locations using imported distance csv file
def getDistance(location1, location2):
    d = csv_distance[location1][location2]
    if d == '':  # ignores the blank spaces
        d = csv_distance[location2][location1]
    return float(d)


# This is the function for creating weights for each node
# input a node, and it will find all possible locations it can travel to
# and then divide the number of locations available by the total of all distances
# This is used to provide a bonus to nodes that have many close neighbors
# O(N)
def getWeights(column):
    row_weight = 0
    locations = 0
    for i in csv_distance[column]:
        if i != '':
            row_weight += float(i)
            locations += 1
    return locations / row_weight


# Function to get the address's index
def getAddress(address):
    for record in csv_address:
        if address in record[2]:
            return int(record[0])


# This is the class for my delivery algorithm:
# Nearest Neighbor is implemented but with a weight system
# based on the percentage of potential locations and the
# distance traveled between them
# Time complexity: O(n^2) if regular nearest neighbor, O(n^3) with weighted option
# although this can be optimized
def delivery(truck):
    # Initialize a list for packages that are yet to be delivered
    packages_to_deliver = []

    # loop through the packages assigned to the truck and add them to the 'packages_to_deliver' list
    for packageID in truck.packages:  # O(N)
        package = package_hash.lookup(packageID)
        packages_to_deliver.append(package)

    # Clear up the packages associated with the truck
    truck.packages.clear()

    # Run while there are packages waiting to be delivered
    while packages_to_deliver:  # O(N)
        lowest_weighted_mileage = 1000
        lowest_mileage = 1000
        current_package = None

        # Loop through all the packages in the 'packages_to_deliver' list and compare each distance to the stored
        # 'lowest_mileage', this finds the lowest overall distance for the next delivery
        for package in packages_to_deliver:  # O(N)
            weight = getWeights(getAddress(package.address))  # getWeights is O(N)
            if (getDistance(getAddress(truck.address), getAddress(package.address))) \
                    * weight <= lowest_weighted_mileage:
                lowest_mileage = getDistance(getAddress(truck.address), getAddress(package.address))
                lowest_weighted_mileage = \
                    getDistance(getAddress(truck.address), getAddress(package.address)) \
                    * weight

                current_package = package

        # Once the shortest path is discovered, the package is loaded on the truck,
        truck.packages.append(current_package.pid)
        packages_to_deliver.remove(current_package)

        # the truck mileage increases with the new delivery, the trucks location is updated
        # to reflect where it has just delivered the package, the departure time is updated
        # and the time the package left the facility to the time it was delivered is updated
        truck.mileage += lowest_mileage
        truck.address = current_package.address
        truck.time += datetime.timedelta(hours=lowest_mileage / 18)
        current_package.delivery = truck.time
        current_package.departure = truck.departure
