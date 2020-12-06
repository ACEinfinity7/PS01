

class BinToHex:

    hexLookup = ['1', '2', '3', '4', '5', '6', '7', '8', \
                 '9', 'a', 'b', 'c', 'd', 'e', 'f']

    def __init__(self, bits):
        #input is a binary number
        self.bits = bits
        self.hexVals = ""

    def convert(self):
        #break off bits until inputted bit value is zero
        while self.bits > 0:
            #capture the 4 rightmost bits
            currVal = self.bits & 0xf

            #insert new value to output by indexing
            #char to a list of possible chars
            self.hexVals = self.hexLookup[currVal-1] + self.hexVals

            #shift the value by the 4 bits you just examined
            self.bits = self.bits >> 4


binToHex = BinToHex(0b10011101)
binToHex.convert()
print(binToHex.hexVals)

# print(bin(0b10011101))
# print(bin(0b10011101 & 0xf))
# print(bin((0b10011101 >> 4) & 0xf))


# print(BinToHex([0,0,0,0]))
# print(BinToHex([1,0,0,0]))
# print(BinToHex([0,1,0,0]))
# print(BinToHex([1,1,0,0]))
# print(BinToHex([0,0,1,0]))
# print(BinToHex([1,0,1,0]))
# print(BinToHex([0,1,1,0]))
# print(BinToHex([1,1,1,0]))
# print(BinToHex([0,0,0,1]))
# print(BinToHex([1,0,0,1]))
# print(BinToHex([0,1,0,1]))
# print(BinToHex([1,1,0,1]))
# print(BinToHex([0,0,1,1]))
# print(BinToHex([1,0,1,1]))
# print(BinToHex([0,1,1,1]))
# print(BinToHex([1,1,1,1]))
