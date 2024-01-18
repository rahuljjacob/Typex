class Stator:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, statorperm):
        self.newdict = {}    #encryption dictionary
        self.decdict = {}    #decryption dictionary
        self.statorperm = statorperm
        self.mapdictionary()

    def mapdictionary(self):
        for(i, j) in zip(self.alphabet, self.statorperm):
            self.newdict[i] = j
            self.decdict[j] = i

    def decrypt(self, i):
            return self.decdict[i]

    def encrypt(self, i):
        return self.newdict[i]

class Rotor:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, rotorperm, notch_count, rotorposition): 
        self.encdict = {}                                       #Encryption Dictionary
        self.decdict = {}                                       #Decryption Dictionary
        self.count = 0
        self.notch_count = notch_count                          #Determines how many letters the rotor should take before rotating once
        self.rotorperm = (rotorperm)                            #Random rotor permutation
        self.rotorposition = rotorposition                      #Initial starting position
        self.mapdictionary()
        self.setrotorpos()

    #Creates both the encryption and decryption dictionaries
    def mapdictionary(self):
        for(i, j) in zip(self.alphabet, self.rotorperm):
            self.encdict[i] = j
        for(i, j) in zip(self.rotorperm, self.alphabet):
            self.decdict[i] = j
    
    #Temporary function to debug, prints both dictionaries 
    def displayenc(self):
        for k, v in self.encdict.items():
            print(k, v)
        print("--------------")

    
    def displaydec(self):
        for k, v in self.decdict.items():
            print(k, v)
        print("--------------")
    
    #Shifts the dictionary backwards, used for decryption
    def reverse_shift_dictionary_values(self, d):
        if not d:
            return {}

        keys = list(d.keys())
        values = list(d.values())
        shifted_values = [values[-1]] + values[:-1]
        shifted_dict = {keys[i]: shifted_values[i] for i in range(len(keys))}
    
        return shifted_dict

    #Shifts the dictionary forwards, used for encryption 
    def forward_shift_dictionary_values(self, d):
        if not d:
            return {}

        keys = list(d.keys())
        values = list(d.values())
        reversed_values = values[1:] + [values[0]]
        reversed_dict = {keys[i]: reversed_values[i] for i in range(len(keys))}

        return reversed_dict

    def encrypt(self, i):
        self.count += 1
        return self.encdict[i] 

    def decrypt(self, i):
        self.count += 1
        return self.decdict[i]
    
    def checkrotorstatus_encryption(self):
        if(self.count == self.notch_count):
                self.encdict = self.forward_shift_dictionary_values(self.encdict)
                self.count = 0

    def checkrotorstatus_decryption(self):
        if(self.count == self.notch_count):
            self.decdict = self.reverse_shift_dictionary_values(self.decdict) #have to change
            self.count = 0
 
    def setrotorpos(self):
        for _ in range(self.rotorposition):     # _ avoids using an iterator variable
            self.encdict = self.forward_shift_dictionary_values(self.encdict)
            self.decdict = self.reverse_shift_dictionary_values(self.decdict)

mappings = { 
        'L':'X',
        'X':'L',
        'J':'A',
        'A':'J',
        'S':'O',
        'O':'S',
        'G':'Q',
        'Q':'G',
        'U':'P',
        'P':'U',
        'V':'Z',
        'Z':'V',
        'R':'B',
        'B':'R',
        'N':'Y',
        'Y':'N',
        'F':'C',
        'C':'F',
        'T':'D',
        'D':'T',
        'M':'I',
        'I':'M',
        'E':'K',
        'K':'E',
        'H':'W',
        'W':'H',
}

def reflector(i):
    return mappings[i]

#Test to make sure the Stator is working

#stator1 = Stator("QVNGWDUCBREIXKTLJMYPSHAOZF")
#for i in "ABCD":
#    print(stator1.encrypt(i), end = '')
#
#print()
#
#for i in "QVNG":
#    print(stator1.decrypt(i), end = '')


#Test to make sure Rotor is Working

#rotor1 = Rotor("WVCSFLDOXAQNHPUGITZKYBEJMR", 1, 0)
#for i in "ABCD":
#    print(rotor1.encrypt(i), end = '')
#    rotor1.checkrotorstatus_encryption()
#
#print()
#
#rotor2 = Rotor("WVCSFLDOXAQNHPUGITZKYBEJMR", 1, 0)
#for i in "WCFD":
#    print(rotor2.decrypt(i), end = '')
#    rotor2.checkrotorstatus_decryption()
