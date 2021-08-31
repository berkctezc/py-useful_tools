import pyperclip as pc  # pip install pyperclip
import math
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printSplitted(string):
    print(bcolors.OKGREEN+"==========="+bcolors.ENDC)
    print(bcolors.OKCYAN+string+bcolors.ENDC)
    print(bcolors.OKGREEN+"==========="+bcolors.ENDC)


def distance(lat1, lon1, lat2, lon2, unit):
    if (lat1 == lat2) and (lon1 == lon2):
        return 0
    else:
        theta = lon1-lon2
        dist = math.sin(math.radians(lat1)) * math.sin(math.radians(lat2)) + math.cos(
            math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(theta))
        dist = math.acos(dist)
        dist = math.degrees(dist)
        miles = dist * 60 * 1.1515
        unit = unit.upper()

        if unit == 'K':
            return miles * 1.609344
        elif unit == 'M':
            return miles * 1.609344 * 1000
        elif unit == 'N':
            return miles * 0.8684
        else:
            return miles


def main():
    counter = 0

    print("Pass 0 to return to origin")

    unit = 'M'  # unit = str(input('* Enter unit of measurement: ')).upper()
    originLat = float(input('* Origin Latitude: '))
    if(originLat == 0):
        print("Terminated script")
        sys.exit()
    originLon = float(input('* Origin Longitude: '))
    if(originLon == 0):
        print("Terminated script")
        sys.exit()

    while True:
        destinationLat = float(input('* Destination Latitude: '))
        if(destinationLat == 0):
            break
        destinationLon = float(input('* Destination Longitude: '))
        if(destinationLon == 0):
            break

        calculatedDistance = math.floor(distance(originLat, originLon,
                                                 destinationLat, destinationLon, unit))
        pc.copy(str(calculatedDistance))
        printSplitted(str(calculatedDistance) + " " + unit)
        printSplitted("COPIED TO CLIPBOARD")

        counter += 1
        printSplitted(str(counter) + " distance(s) calculated with origin:" +
                      str(originLat)+"," + str(originLon))


while True:
    print(bcolors.HEADER+"Calculator started / Pass 0 to exit the script."+bcolors.ENDC)
    main()
