#  Joshua Hillary
#  Student ID: 005250603
import datetime
import PrettyText
from HashMap import loadPackageData, package_hash
from Trucks import truck1, truck2, truck3
from Delivery import delivery

# Calls the function located in HashMap to load the package csv into the hashmap
loadPackageData("CSV_Packages.csv")

# Call the 'delivery' function which runs nearest neighbor and input each truck
delivery(truck1)
delivery(truck2)
truck3.departure = min(truck1.time, truck2.time)  # Ensures truck3 leaves at the earliest time
delivery(truck3)

console = ""
PrettyText.print_welcome()  # Prints the welcome flag
# Command Line Interface for interfacing with user
while console.lower() not in ['exit', 'quit']:
    console = input(PrettyText.print_yellow("->"))

    # User can print the details of all three trucks
    if console.lower() in ['trucks', 'truck']:
        print(PrettyText.print_green(str(truck1) + "\n" +
                                     str(truck2) + "\n" +
                                     str(truck3)))

    elif console.lower() in ['checkpoint']:
        try:
            time_input = input(PrettyText.print_green('Enter the time you\'d like to check the package status ('
                                                      'HH:MM:SS)\n'))
            (hrs, mins, secs) = time_input.split(':')
            convert_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

            package_input = input(PrettyText.print_green("Enter a package ID # or type 'All'\n"))
            if package_input in ['all']:
                try:
                    for pID in range(1, 41):
                        package = package_hash.lookup(pID)
                        package.set_status(convert_time)
                        print(PrettyText.print_green(str(package)))

                except ValueError:
                    print(PrettyText.print_green("Something went wrong with this operation"))
            else:
                try:
                    package = package_hash.lookup(int(package_input))
                    package.set_status(convert_time)
                    print(PrettyText.print_green(str(package)))

                except ValueError:
                    print(PrettyText.print_green("Package ID or input not found"))
        except ValueError:
            print(PrettyText.print_green("Error: format of time should be in ('HH:MM:SS')"))

    # Opens the package menu, where users can choose to see all packages or enter an ID for one package
    elif console.lower() in ['packages']:
        prompt = input(PrettyText.print_green("Enter an ID number or 'All'\n"))
        if prompt.lower() in ['all']:
            for i in range(41):
                print(PrettyText.print_green(str(package_hash.lookup(i))))
        else:
            print(PrettyText.print_green(str(package_hash.lookup(int(prompt)))))

    # Prints the total truck mileage after all packages have been delivered
    elif console.lower() in ['total truck mileage']:
        print(PrettyText.print_green("Route mileage at the end of the day:   " +
                                     str(truck1.mileage +
                                         truck2.mileage +
                                         truck3.mileage)))

    # Closes the console loop
    elif console.lower() in ['exit', 'quit']:
        pass

    # Opens the help menu
    elif console.lower() in ['help', 'help me']:
        PrettyText.print_help()

    # When an unacceptable input is entered, remind the user of the 'help' command
    else:
        print(PrettyText.print_green("Unknown input -> "))
        print(PrettyText.print_green("Type 'Help' to view the list of commands"))

else:
    print(PrettyText.print_green("Console Stream Terminated"))
