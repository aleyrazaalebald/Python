# We want to model DNA Sequence in Python. 
# A DNA Sequence is an object. DNA Sequence comprises of series of characters A, T, G, C
# An example DNA looks like:
# CAATCTATTTAAAGTAATCCCTTATGTAGCGTCTGACTAGCTAGCCCCTAGGATGCCCATGAGAGTACGATGACG..... 
#
# Required Attributes:
#   The sequence itself
#   Length  -> computed via a method or function
#   Percent {A,T,G,C} -> computed via a method or function
#   GC content -> computed ia a method or function

# Required Methods:
#   calculate subsequences within DNA Sequence    
#   mismatch counts and positions in DNA Sequence
#   reversing the dna sequence
#   

####################################################################################
# if you look at above class, then we see that first attributes were searched, and 
# thought if they will be set from outside at the time of object instantiation. 
# similarly, the operation related with dna sequence also decided and written.  
# SO THIS MAKES OUR DNA SEQUENCE CLASS COMPLETE (both data structure an operations)
####################################################################################
#
# example implementation of required class.

def reverseComplement(dnaSequence):
    complementTable ={"A": "T",
                      "C":"G",
                      "G":"C",
                      "T":"A",
                      "N":"N"}
    revComp = ""
    for base in dnaSequence[::-1]: # ::-1 -> from the start till end iterate backward over each element.
        revComp += complementTable[base]
    return revComp

class DNASequence(object):
    def __init__(self, sequence: str):
        self.sequence = sequence.upper() 
        self.length = len(sequence)
        self.percentBase = self.getPercentBases()
        self.gcContent = self.getGCContent()
        self.reverseComplement = reverseComplement(self.sequence)

    def getPercentBases(self): 
        # go through sequence chacters and add each unique character 
        # with number of occurance in dictionary.
        collection = {}
        for base in self.sequence:
            if base not in collection:
                collection[base] = 0
            collection[base] += 1

        # now go through collection dictionary and replace each unique 
        # character occurance with is percentage
        for base in collection:
            collection[base] = collection[base] / self.length
        return collection

    def getGCContent(self):
        totalPercent = 0
        for base in ["G", "C"]:
            if base in self.percentBase:
                totalPercent += self.percentBase[base]
            else:
                totalPercent += 0 # not absolutely necessary
        return totalPercent
    def countMismatches(self, otherSequence):
        #type checking
        assert type(otherSequence) == str, "Error, sequence for comparsion must be a string type."
        if not len(self.sequence) == len(otherSequence):
            raise ValueError("Both sequence must be the same length for comparison")
        otherSequence = otherSequence.upper()
        mismatches = 0
        # iterate for loop over position
        for i in range(len(self.sequence)):
            if self.sequence[i] != otherSequence[i]:
                mismatches += 1
        return mismatches

    # to string method implementation
    def __str__(self):
        return "sequence is: " + self.sequence

# to test the dna class
if __name__ == "__main__":
    test = DNASequence("ATGCATGCTGACCTGAGCTAATGCGATCGTCACGTACAGTTGCACAGTGTCAAAAA")

    #testing count mismatch method
    otherseq = "ATGCATGCTGACCTGAGCTAATGCGATCGTCACGTACAGTTGCACAGTGTCAAAAA"
    assert test.countMismatches(otherseq) == 0, "expected result 0"
    print(test)  # calling to string implementation
    print(test.__dict__) # calling dictionary

