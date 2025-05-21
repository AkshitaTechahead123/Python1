class MathHelper:
    pi = 3.14  # static/class variable

    @staticmethod
    def area_of_circle(radius):
        return MathHelper.pi * radius ** 2

# Test
print(MathHelper.area_of_circle(5))  # Output: 78.5
