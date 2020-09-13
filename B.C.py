class SignedBit():

    def __init__(self, val):
        #4 bit array, val domain is 7 to -7
        self.val = abs(val)
        #little endian bit array
        self.bitArray = []
        #convert val to bit array
        while self.val > 0:
            #take next bit
            remainder = self.val & 1
            print(remainder)
            #add bit to bitArray as str
            self.bitArray.append(str(remainder))
            #remove that bit
            self.val = self.val >> 1

        while len(self.bitArray) < 3:
            self.bitArray.append("0")

        if val == abs(val):
            self.bitArray.append("0")

        else:
            self.bitArray.append("1")

    def __add__(self, other):
        resultArray = []
        carry = 0
        for (a,b) in zip(self.bitArray, other.bitArray):
            #build up a counter if it encounters 1s
            #if counter is 3, it places a 1
            #if counter is 2, it carries a 1
            #if counter is 1, it places a 1

            counter = carry

            counter += 1 if a == "1" else 0
            counter += 1 if b == "1" else 0

            resultArray.append("1" if counter == 1 or counter == 3 else "0")

            carry = 0 if counter < 2 else 1
        return resultArray


    def negate(self):
        #if signed bit is 0 change to 1 and vice versa
        if self.bitArray[-1] == "0":
            self.bitArray[-1] = "1"

        else:
            self.bitArray[-1] = "0"



signedBit = SignedBit(3)
print(signedBit.bitArray)
print(signedBit.val)
print("hello")

signedBit2 = SignedBit(2)
print(signedBit2.bitArray)
print(signedBit2.val)

print(signedBit + signedBit2)
