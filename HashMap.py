import csv
import Packages


# Create Hash Map class
class CreateHashMap:
    def __init__(self, initial_capacity=20): # default capacity
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Inserts an item into the hashtable by inserting a key and item pair as parameters
    def insert(self, key, item):
        # get the bucket list location
        # where this item will go by modding the key by the size of the list
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # O(N) if the key is already in the bucket
        # then the item is updated
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # If it's a new key and item
        # then both key and item are added
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # This is the function to look up an item by providing a key
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        # if the key does not exist
        return None

    # Removes the item from the table by providing a key
    def remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        # If the key exists then the item and key are removed
        if key in destination:
            destination.remove(key)


# Calls the 'CreateHashMap' function to instantiate a hash table for packages
package_hash = CreateHashMap()


# This function opens the csv and loads contents into 'package_hash'
def loadPackageData(filename):
    with open(filename) as csv_pack:
        csv_packages = csv.reader(csv_pack)
        csv_packages = list(csv_packages)
        for package in csv_packages:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            # the temporary package object that is inserted into the package hash
            p = Packages.Packages(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)
            package_hash.insert(pID, p)
