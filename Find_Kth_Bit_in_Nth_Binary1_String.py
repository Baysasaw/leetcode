class Solution:
    def reverse(self, x: str) -> str:
        return x[::-1]

    def invert(self, x: str) -> str:
        return ''.join('1' if bit == '0' else '0' for bit in x)

    def findKthBit(self, n: int, k: int) -> str:
        carnt = "0"
        if n == 1:
            return "0"
    
        for i in range(1, n):
            carnt = carnt + "1" + self.reverse(self.invert(carnt))
        return carnt[k-1]
