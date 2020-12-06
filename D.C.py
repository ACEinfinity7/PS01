class twosComplement():

    def __init__(self, val, size):
        self.size = size
        self.binString = ""
        self.val = abs(val)

        #convert val to binary number
        while self.val > 0:
            rem = self.val & 1
            self.binString = str(rem) + self.binString
            self.val = self.val >> 1
        #zero pad
        while len(self.binString) < self.size:
            self.binString = "0" + self.binString
        #use the trick of negating and adding one to negate binaryString
        if self.val != abs(val):
            self.binString = twosComplement.negate(self.binString)
            self.binString = twosComplement.add(self.binString)



    @staticmethod
    def add(binString, otherVal="0001"):
        resultString = ""
        carry = 0
        for (a,b) in zip(binString[::-1], otherVal[::-1]):
            #build up a counter if it encounters 1s
            #if counter is 3, it places a 1
            #if counter is 2, it carries a 1
            #if counter is 1, it places a 1

            counter = carry

            counter += 1 if a == "1" else 0
            counter += 1 if b == "1" else 0

            if counter == 1 or counter == 3:
                resultString = "1" + resultString
            else:
                resultString = "0" + resultString

            carry = 0 if counter < 2 else 1

        return resultString

    @staticmethod
    def negate(binString):
        #flip all bits
        return ''.join('1' if x == '0' else '0' for x in binString)

    @staticmethod
    def binStringToDec (binString):
        #makes binString positive and sets a -1 mult for final value
        if binString[0] == "1":
            workingString = twosComplement.negate(binString)
            workingString = twosComplement.add(workingString)
            sign = -1
        else:
            sign = 1

        val = 0
        mult = 1
        #convert bit array to decimal value
        for i in workingString[::-1]:
            val += int(i) * mult
            mult *= 2
        #add correct sign to decimal value
        val *= sign

        return val

    def __str__(self):
        return str(twosComplement.binStringToDec(self.binString))

    def __add__(self, other):
        #add the two binStrings
        addResult = twosComplement.add(self.binString,other.binString)
        #convert the String result to decimal
        addResultString = twosComplement.binStringToDec(addResult)
        #create a new object with that val in it
        resultObj = twosComplement(addResultString,self.size)
        return resultObj

two = twosComplement(-4, 4)
print(two.binString)
print(two)
two2 = twosComplement (-4,4)


print('ttttt')

two3 = two+two2
print(two3)
