class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        print self.miles
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        print self.miles
        return self

riding = Bike(1000, "25mph", 0)
print riding.ride().ride().ride().reverse().displayInfo()
