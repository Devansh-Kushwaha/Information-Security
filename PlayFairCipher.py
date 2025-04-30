print("Welcome to the Play Fair Cipher.")
print("What do you wish to do?")

program = True

while program:
    print("1. Encryption")
    print("2. Decryption")
    print("3. End Program")
    choice = input("Enter your choice: ")

    if choice == "1":
        # f = input("Enter the file name or relative path: ")
        f = "plaintext.txt"
        ke = input("Enter the cipher key: ")
        with open(f, "r") as infile:
            data = infile.read()

        text = ""
        for i in data:
            if i.isalnum():
                text += i.upper()

        keymatrix = [[""] * 6 for _ in range(6)]
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        ke = ke.upper()

        for i in alphabets:
            if i not in ke:
                ke += i

        key = ""
        for i in ke:
            if i not in key and i.isalnum():
                key += i

        index = 0
        for i in range(6):
            for j in range(6):
                keymatrix[i][j] = key[index]
                index += 1

        d = {}
        for i in range(6):
            for j in range(6):
                d[keymatrix[i][j]] = [i, j]
        print("KEY",keymatrix)

        pairs = []
        index = 0
        while index < len(text):
            temp = []
            temp.append(text[index])
            index += 1
            if index < len(text):
                if text[index] == temp[0]:
                    temp.append("X")
                else:
                    temp.append(text[index])
                    index += 1
            else:
                temp.append("X")
            pairs.append(temp)

        # Encryption
        encryptedpairs = []
        for pair in pairs:
            coordinate1 = d[pair[0]].copy()
            coordinate2 = d[pair[1]].copy()

            if coordinate1[0] == coordinate2[0]:
                coordinate1[1] = (coordinate1[1] + 1) % 6
                coordinate2[1] = (coordinate2[1] + 1) % 6
            elif coordinate1[1] == coordinate2[1]:
                coordinate1[0] = (coordinate1[0] + 1) % 6
                coordinate2[0] = (coordinate2[0] + 1) % 6
            else:
                coordinate1[1], coordinate2[1] = coordinate2[1], coordinate1[1]

            encryptedpair = [
                keymatrix[coordinate1[0]][coordinate1[1]],
                keymatrix[coordinate2[0]][coordinate2[1]],
            ]
            encryptedpairs.append(encryptedpair)

        enc = ""
        for i in encryptedpairs:
            enc += i[0] + i[1]

        print("Encrypted data: ", enc)
        with open("cipher.txt", "w") as outfile:
            outfile.write(enc)
        print("Encrypted message stored in cipher.txt")

    elif choice == "2":
        f = "cipher.txt"
        ke = input("Enter the cipher key: ")
        with open(f, "r") as infile:
            data = infile.read()

        text = ""
        for i in data:
            text += i.upper()

        keymatrix = [[""] * 6 for _ in range(6)]
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        ke = ke.upper()

        for i in alphabets:
            if i not in ke:
                ke += i

        key = ""
        for i in ke:
            if i not in key and i.isalnum():
                key += i

        index = 0
        for i in range(6):
            for j in range(6):
                keymatrix[i][j] = key[index]
                index += 1

        d = {}
        for i in range(6):
            for j in range(6):
                d[keymatrix[i][j]] = [i, j]

        pairs = []
        index = 0
        while index < len(text):
            temp = []
            temp.append(text[index])
            index += 1
            temp.append(text[index])
            index += 1
            pairs.append(temp)

        # Decryption
        decryptedpairs = []
        for pair in pairs:
            coordinate1 = d[pair[0]].copy()
            coordinate2 = d[pair[1]].copy()

            if coordinate1[0] == coordinate2[0]:
                coordinate1[1] = (coordinate1[1] - 1) % 6
                coordinate2[1] = (coordinate2[1] - 1) % 6
            elif coordinate1[1] == coordinate2[1]:
                coordinate1[0] = (coordinate1[0] - 1) % 6
                coordinate2[0] = (coordinate2[0] - 1) % 6
            else:
                coordinate1[1], coordinate2[1] = coordinate2[1], coordinate1[1]

            decryptedpair = [
                keymatrix[coordinate1[0]][coordinate1[1]],
                keymatrix[coordinate2[0]][coordinate2[1]],
            ]
            decryptedpairs.append(decryptedpair)

        dec = ""
        for i in decryptedpairs:
            dec += i[0] + i[1]

        dec = dec.replace("X", "")
        print("Decrypted data: ", dec)
        with open("recover.txt", "w") as outfile:
            outfile.write(dec)
        print("Recovered message stored in recover.txt")

    else:
        program = False
