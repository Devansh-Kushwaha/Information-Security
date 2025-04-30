print("Welcome to the Caesar Cipher.")
print("What do you wish to do?")
program = True

while program:
    print("1. Encryption / Decryption")
    print("2. Cryptanalysis")
    print("3. End Program")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("1. Encryption")
        print("2. Decryption")
        choice2 = input("Enter your choice: ")

        if choice2 == "1":
            f = input("Enter the file name or relative path: ")
            key = int(input("Enter the cipher key: "))

            with open(f, "r") as infile:
                data = infile.read()

            enc = ""
            for i in data:
                if ord(i):
                    o = (ord(i) + key) % 128
                    enc += chr(o)
                else:
                    enc += i

            with open("Cipher.txt", "w") as outfile:
                outfile.write(enc)

            print("Encrypted data:", enc)
            print("Encrypted message stored in Cipher.txt")

        elif choice2 == "2":
            f = input("Enter the file name or relative path: ")
            key = int(input("Enter the cipher key: "))

            with open(f, "r") as infile:
                data = infile.read()

            dec = ""
            for i in data:
                if ord(i):
                    o = (ord(i) - key) % 128
                    dec += chr(o)
                else:
                    dec += i

            with open("Decrypted.txt", "w") as outfile:
                outfile.write(dec)

            print("Decrypted data:", dec)
            print("Decrypted message stored in Decrypted.txt")

    elif choice == "2":
        print("1. Brute Force Approach")
        print("2. Frequency Analysis Approach")
        choice2 = input("Enter your choice: ")

        if choice2 == "1":
            f = input("Enter the file name or relative path: ")
            Words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
                     "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would",
                     "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like",
                     "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
                     "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our",
                     "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]
            List = []

            with open(f, "r") as infile:
                data = infile.read()

            for key in range(0, 26):
                sc = 0
                dec = ""
                for i in data:
                    if ord(i):
                        o = (ord(i) - key) % 128
                        dec += chr(o)
                    else:
                        dec += i
                spl = dec.split(" ")
                for word in spl:
                    for fixes in Words:
                        if fixes.upper() == word.upper():
                            sc += 1
                List.append((sc, dec, key))

            List.sort()
            print("Key =", List[-1][2])
            print("Most probable output:", List[-1][1])
            with open("Recover.txt", "w") as outfile:
                outfile.write(List[-1][1])
            print("Recovered message stored in Recover.txt")

        elif choice2 == "2":
            f = input("Enter the file name or relative path: ")
            List = []
            d = [" ", "E", "T", "A", "O", "I", "N", "S", "H", "R", "D", "L", "C", "U", "M", "W", "F", "G", "Y", "P"]
            Words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
                     "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would",
                     "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like",
                     "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
                     "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our",
                     "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]

            with open(f, "r") as infile:
                data = infile.read()

            dic = {}
            for letter in data:
                if letter.upper() in dic:
                    dic[letter.upper()] += 1
                else:
                    dic[letter.upper()] = 1

            maxchar = ""
            value = 0
            data = data.upper()

            for letter in dic:
                if dic[letter] > value:
                    maxchar = letter
                    value = dic[letter]

            for k in range(len(d)):
                character = d[k]
                key = ord(maxchar) - ord(character)
                dec = ""
                for i in data:
                    if ord(i):
                        o = (ord(i) - key) % 128
                        dec += chr(o)
                    else:
                        dec += i
                sc = 0
                spl = dec.split(" ")
                for word in spl:
                    for fixes in Words:
                        if fixes.upper() == word.upper():
                            sc += 1
                if sc / len(spl) >= 0.3:
                    print("Key =", key)
                    print("Decrypted data:", dec)
                    with open("Recover.txt", "w") as outfile:
                        outfile.write(dec)
                    print("Recovered message stored in Recover.txt")
                    break
            else:
                print("No key matches the 30% mark")

    elif choice == "3":
        program = False
