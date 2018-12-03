class ApartmentAd:

    def __init__(self,rooms,price,address,latitude,longtitude,type):
        self.rooms = rooms
        self.price = price
        self.address = address
        self.latitude = latitude
        self.longtitude = longtitude
        self.type = type

    def validate(self):
        if self.rooms <= 0:
            print("Invalid number of rooms")
            exit(-1)
        if self.price <= 0:
            print("Invalid price")
            exit(-1)
        if type < 0 or type > 3:
            print("Invalid type")
            exit(-1)

