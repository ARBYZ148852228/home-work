class Temperature:
    def __init__(self, celsius):
        self.__Celsius = celsius

    def to_fahrenheit(self):
        return self.__Celsius * 9 / 5 + 32

    def get_celsius(self):
        return self.__Celsius

temp = Temperature(25)
print(temp.to_fahrenheit())
print(temp.get_celsius())









