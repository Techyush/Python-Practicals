class Hardware:
    devices = "Motherboard"

    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost


ryzen = Hardware("Ryzen", "10000")
gigabyte = Hardware("Gigabyte", "7500")

print("Ryzen is a {}".format(ryzen.__class__.devices))
print("Gigabyte is also a {}".format(gigabyte.__class__.devices))

print("{} price is {} only".format(ryzen.brand, ryzen.cost))
print("{} price is {} only".format(gigabyte.brand, gigabyte.cost))