# https://leetcode.com/problems/convert-the-temperature
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [self.toKelven(celsius), self.toFahrenheit(celsius)]

    def toKelven(self, celsius: float) -> float:
        return celsius + 273.15

    def toFahrenheit(self, celsius: float) -> float:
        return celsius * 1.80 + 32.00
