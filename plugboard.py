def Plugboard(plaintext):
    plaintext = plaintext.upper()
    plainlist = []

    for i in plaintext:
        plainlist.append(i)

    plugboard_setting = { 
        'A' : 'A',
        'B' : 'B',
        'C' : 'C',
        'D' : 'D',
        'E' : 'E',
        'F' : 'F',
        'G' : 'G',
        'H' : 'H',
        'I' : 'I',
        'J' : 'J',
        'K' : 'K',
        'L' : 'L',
        'M' : 'M',
        'N' : 'N',
        'O' : 'O',
        'P' : 'P',
        'Q' : 'Q',
        'R' : 'R',
        'S' : 'S',
        'T' : 'T',
        'U' : 'U',
        'V' : 'V',
        'W' : 'W',
        'X' : 'X',
        'Y' : 'Y',
        'Z' : 'Z',
        ' ' : ' ',
    }

    plugtext = []

    changes = input("Do you need Plugboard Changes (Y/N): ").lower()
    if(changes == 'y'):
        cycles = 'y'
        while(cycles == 'y'):
            a = input("Character : ").upper()
            b = input("Goes To: ").upper()
            plugboard_setting[a] = b
            while (plugboard_setting[b] == b):
                a = input("Character : ").upper()
                b = input("Goes To: ").upper()
                plugboard_setting[a] = b
            cycles = input("Would you like to Make More Changes(y/n) : ")

    for i in plainlist:
        plugtext.append(plugboard_setting[i])

    plugboard_string = ''.join(plugtext)
    return plugboard_string

