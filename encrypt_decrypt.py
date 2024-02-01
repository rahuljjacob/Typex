import plugboard
import rotors_stators

statorperm1 = "QVNGWDUCBREIXKTLJMYPSHAOZF"
statorperm2 = "YBQGOXHWIZPKNTFEAUVJRSLMDC"


rotorperm1 = "WVCSFLDOXAQNHPUGITZKYBEJMR"
rotorperm2 = "JABIVYKSWFROQPXNGETDMCZLHU"
rotorperm3 = "WJTLAUORKFNSMQCPEYIXHBZGDV"

def totalencryption(plaintext, rotor_position):

    ciphertextlist = []
    
    plugboard_string = plugboard.Plugboard(plaintext)

    stator1 = rotors_stators.Stator(statorperm1)
    stator2 = rotors_stators.Stator(statorperm2)
    rotor1 = rotors_stators.Rotor(rotorperm1, 2, rotor_position[0])
    rotor2 = rotors_stators.Rotor(rotorperm2, 8, rotor_position[1])
    rotor3 = rotors_stators.Rotor(rotorperm3, 14, rotor_position[2])

    
    for i in plugboard_string:
        s1c1 = stator1.encrypt(i)
        s2c1 = stator2.encrypt(s1c1)
        r1c1 = rotor1.encrypt(s2c1)
        r2c1 = rotor2.encrypt(r1c1)
        r3c1 = rotor3.encrypt(r2c1)
        mappedletter = rotors_stators.reflector(r3c1)
        r3c2 = rotor3.encrypt(mappedletter)
        r2c2 = rotor2.encrypt(r3c2)
        r1c2 = rotor1.encrypt(r2c2)
        s2c2 = stator2.encrypt(r1c2)
        s1c2 = stator1.encrypt(s2c2)

        ciphertextlist.append(s1c2)
        
        rotor1.checkrotorstatus_encryption()
        rotor2.checkrotorstatus_encryption()
        rotor3.checkrotorstatus_encryption()


        

    ciphertext = ''.join(ciphertextlist)
    return ciphertext

def totaldecryption(ciphertext, rotor_position):
    
    plaintextlist = []
    
    plugboard_string = plugboard.Plugboard(ciphertext)
    
    stator1 = rotors_stators.Stator(statorperm1)
    stator2 = rotors_stators.Stator(statorperm2)
    rotor1 = rotors_stators.Rotor(rotorperm1, 2, rotor_position[0])
    rotor2 = rotors_stators.Rotor(rotorperm2, 8, rotor_position[1])
    rotor3 = rotors_stators.Rotor(rotorperm3, 14, rotor_position[2])

    for i in plugboard_string:
        s1c1 = stator1.decrypt(i)
        s2c1 = stator2.decrypt(s1c1)
        r1c1 = rotor1.decrypt(s2c1)
        r2c1 = rotor2.decrypt(r1c1)
        r3c1 = rotor3.decrypt(r2c1)
        mappedletter = rotors_stators.reflector(r3c1)
        r3c2 = rotor3.decrypt(mappedletter)
        r2c2 = rotor2.decrypt(r3c2)
        r1c2 = rotor1.decrypt(r2c2)
        s2c2 = stator2.decrypt(r1c2)
        s1c2 = stator1.decrypt(s2c2)

        plaintextlist.append(s1c2)

        rotor1.checkrotorstatus_decryption()
        rotor2.checkrotorstatus_decryption()
        rotor3.checkrotorstatus_decryption()


    plaintext = ''.join(plaintextlist)
    return plaintext


#rotor = [0,1,1]
#
#string1 = totalencryption('ABCD', rotor)
#print(string1)
#
#string2 = totaldecryption(string1 , rotor)
#print(string2)
