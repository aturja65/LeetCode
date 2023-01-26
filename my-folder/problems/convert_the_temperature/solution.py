class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        fahrenheit = (celsius * 1.8) + 32
        kelvin = celsius + 273.15
        return [kelvin, fahrenheit] 