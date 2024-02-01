import encrypt_decrypt

while(1):
    a = input("Would you like to encrypt or decrypt a message (e/d/exit): ").lower()
    
    if(a == "e"):
        print("Enter the Rotor Positions : ")
        epos1 = input("Rotor Position (0: 25) : ")
        epos2 = input("Rotor Position (0: 25) : ")
        epos3 = input("Rotor Position (0: 25) : ")
        plaintext = input("Enter Message to encrypt : ")
        print(encrypt_decrypt.totalencryption(plaintext, [int(epos1), int(epos2), int(epos3)]))
        
    elif(a == "d"):
        print("Enter the Rotor Positions : ")
        dpos1 = input("Rotor Position (0: 25) : ")
        dpos2 = input("Rotor Position (0: 25) : ")
        dpos3 = input("Rotor Position (0: 25) : ")
        ciphertext = input("Enter Message to encrypt : ")
        print(encrypt_decrypt.totaldecryption(ciphertext, [int(dpos1), int(dpos2), int(dpos3)]))

    elif(a == "exit"):
        break
    
    else:
        print("Invalid Option")