class OnesComplement():

    def __init__(self, val):
        #4 bit array, val domain is 7 to -7
        self.val = val
        if self.val != None:
            self.valToArray()

    def valToArray(self):
        self.absVal = abs(self.val)

        if self.val == self.absVal:
            self.sign = "Positive"
        else:
            self.sign = "Negative"

        #little endian bit array
        self.bitArray = []
        #convert val to bit array
        while self.val > 0:
            #take next bit
            remainder = self.val & 1
            #add bit to bitArray as str
            self.bitArray.append(str(remainder))
            #remove that bit
            self.val = self.val >> 1
        #zero pad
        while len(self.bitArray) < 4:
            self.bitArray.append("0")
        #make sure bit array is the correct sign
        if self.sign == "Negative":
            self.negate()


    def __str__(self):
        val = 0
        mult = 1
        #find out if number is negative, if so work with positive verison
        if self.bitArray[-1] == "1":
            array = self.bitArray.negate()
            negate = -1
        else:
            array = self.bitArray
            negate = 1
        #convert bits array to decimal
        for i in array[:-1]:
            val += int(i) * mult
            print(val,mult,i)
            mult *= 2
        #make proper sign
        val *= negate
        return str(val)




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

        #create and return a new class
        resultClass = OnesComplement(None)
        resultClass.bitArray =  resultArray
        return resultClass



    def negate(self):
        #flip all bits
        for i in range(len(self.bitArray)):
            if self.bitArray[i] == "0":
                self.bitArray[i] = "1"

            else:
                self.bitArray[i] = "0"




onesComplement = OnesComplement(3)
print(onesComplement.bitArray)
print(onesComplement.val)
print("hello")

onesComplement2 = OnesComplement(2)
print(onesComplement2.bitArray)
print(onesComplement2.val)

onesComplementAdd = onesComplement + onesComplement2
print(onesComplementAdd.bitArray)

print("break")
print(onesComplementAdd)
