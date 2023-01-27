# Code to format console text
green = '\x1b[6;30;42m'
c_end = '\x1b[0m'
yellow = "\x1b[38;5;157m"


def print_welcome():
    print(green + '-------------------------------------------------------' + c_end)
    print(green + '-------------------------------------------------------' + c_end)
    print(green + '- Welcome to WGUPS: Western Governors Parcel Service! -' + c_end)
    print(green + '-                By: Joshua Hillary                   -' + c_end)
    print(green + '--------------                        -----------------' + c_end)
    print(green + "--------------  type 'help' to start  -----------------" + c_end)
    print(green + '-------------------------------------------------------' + c_end)
    print(green + '-------------------------------------------------------' + c_end)


def print_help():
    print(print_green("<==========================================================>"))
    print(print_green("<==========================================================>"))
    print(print_green("<===============         Help Menu         ================>"))
    print(print_green("<===============           Type:           ================>"))
    print(print_green("<===============   \"Total Truck Mileage\"   ================>"))
    print(print_green("<===============        \"Packages\"         ================>"))
    print(print_green("<===============         \"Trucks\"          ================>"))
    print(print_green("<===============       \"Checkpoint\"        ================>"))
    print(print_green("<===============          \"Exit\"           ================>"))
    print(print_green("<===============                           ================>"))
    print(print_green("<==========================================================>"))
    print(print_green("<==========================================================>"))


def print_green(text):
    return green + text + c_end


def print_yellow(text):
    return yellow + text + c_end
