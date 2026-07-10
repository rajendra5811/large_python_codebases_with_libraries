class House:
    def __init__(self, size, nums_bedrooms, nums_bathrooms):
        self.size = size
        self.beds = nums_bedrooms
        self.baths = nums_bathrooms

    @classmethod
    def create(cls, description):
        size, beds, baths = description.split()
        return cls(float(size), int(beds), int(baths))

    @staticmethod
    def build_door(width, height):
        return (width, height)

    def build_bed(self, bed_type, size):
        print(f"type is {bed_type}")


home = House.create("1000 2 2")
door = House.build_door(5, 7)
home.build_bed("panel footboard", 60 * 70)

print(home.size, home.beds, home.baths)
print(door)


""" Output: type is panel footboard
1000.0 2 2
(5, 7)"""