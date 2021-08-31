import pyperclip as pc  # pip install pyperclip
import math


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

    unit = 'M'  # unit = str(input('* Enter unit of measurement: ')).upper()

    originLat = float(input('* Origin Latitude: '))
    originLon = float(input('* Origin Longitude: '))

    while True:

        destinationLat = float(input('* Destination Latitude: '))
        destinationLon = float(input('* Destination Longitude: '))

        calculatedDistance = math.floor(distance(originLat, originLon,
                                                 destinationLat, destinationLon, unit))
        pc.copy(str(calculatedDistance))
        print(str(calculatedDistance) + " " + unit)
        print("//COPIED TO CLIPBOARD//")

        counter += 1
        print("=========== \n You have calculated " + str(counter) +
              " distance(s) this session. \n===========")


main()
