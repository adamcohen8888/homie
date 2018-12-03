# Homie: adam
# import data from excel file

import sys
import xlrd
from ApartmentAd import *


# Assign spreadsheet fileLocation`
fileName = 'homie_short.xlsx'
fileLocation = "C:/Users/adam/Desktop/homie/homie_short.xlsx"
# Give the location of the file
loc = (fileLocation)
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

#get number of rows and colums
rows = sheet.nrows
#print("rows=", rows)
colums = sheet.ncols
#print ("colums=", colums)

def check_input_values():
    debug = 1 #for debug
    if(len(sys.argv)== 1):#for debug
        find_suitable_apartment(2, 3, 1799, 1801, 4) #for debug
        exit(-100)#for debug
    if(len(sys.argv)!= 6 ):
        print("wrong amount of inputs")
        exit(-1)
    if(int(sys.argv[1])<0):
        print("minimum number of rooms can't be smaller then 0")
        exit(-1)
    if (int(sys.argv[2]) < 0):
        print("maxmium number of rooms can't be smaller then 0")
        exit(-1)
    if (int(sys.argv[2]) < int(sys.argv[1])):
        print("maximum number of rooms can't be smaller then minimum number of rooms")
        exit(-1)
    if (int(sys.argv[3]) < 0):
        print("minimum price can't be smaller then 0")
        exit(-1)
    if (int(sys.argv[4]) < 0):
        print("minimum price can't be smaller then 0")
        exit(-1)
    if (int(sys.argv[4]) < int(sys.argv[3])):
        print("maximum price can't be smaller then minimum price")
        exit(-1)
    if(int(sys.argv[5])<0 or int(sys.argv[5])>3):
        print("invalid type, must be in the range of 0-3")
        exit(-1)


def find_suitable_apartment(min_rooms, max_rooms, min_price, max_price, required_type):
    count = 1
    found_flag = 0
    #print("find_suitable_apartment")#for debug
    for x in range (1, rows):
        rooms = sheet.cell_value(x, 2)
        price = sheet.cell_value(x, 3)
        address = sheet.cell_value(x, 9)
        latitude = sheet.cell_value(x, 10)
        longtitude = sheet.cell_value(x, 11)
        type = sheet.cell_value(x, 12)
        apartment_ad = ApartmentAd(rooms,price,address,latitude,longtitude,type)
        if (min_rooms <= apartment_ad.rooms <= max_rooms ):
            if (min_price <= apartment_ad.price <= max_price ):
                if(required_type == type):
                    print()
                    print ("we found a relevent apartment - ", "apartment number", count)
                    count = count + 1
                    print("number of rooms:", int(apartment_ad.rooms))
                    print("price:", int(apartment_ad.price))
                    if(apartment_ad.address == ""):
                        print("address: wasn't mentioned in the apartment ad")
                    else:
                        print("address:", apartment_ad.address)
                    print("latitude:",int(apartment_ad.latitude))
                    print("longtitude:",int(apartment_ad.longtitude))
                    print("type:",int(apartment_ad.type))
                    found_flag = 1
    if(found_flag == 0):
        print("sorry but we don't have an apartment that sets your request at the moment")

def main():
    check_input_values()
    find_suitable_apartment(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))

if __name__ == "__main__":
    main()


