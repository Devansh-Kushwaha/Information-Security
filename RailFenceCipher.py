print("Welcome to the Rail Fence Cipher.")
print("What do you wish to do?")
program=True
while program:
    print("1. Encryption")
    print("2. Decryption")
    print("3. End Program")
    choice = input("Enter your choice: ")
    if choice == "1":
        f = "plaintext.txt"
        ke = int(input("Enter the cipher key: "))
        with open(f, "r") as infile:
            data = infile.read()

        matrix=[[""]*len(data) for _ in range(ke)]

        row_indices=list(range(ke))+list(range(ke-2,0,-1))
        for i in range(len(data)):
          matrix[row_indices[i%len(row_indices)]][i]=data[i]

        enc=''
        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            enc+=matrix[i][j]
        print("Encrypted Text:",enc)
        with open("cipher.txt", "w") as outfile:
            outfile.write(enc)
        print("Encrypted message stored in cipher.txt")
    elif choice=='2':
      f = "cipher.txt"
      ke = int(input("Enter the cipher key: "))


      with open(f, "r") as infile:
          data = infile.read()

      matrix=[[""]*len(data) for _ in range(ke)]
      row_indices=list(range(ke))+list(range(ke-2,0,-1))
      for i in range(len(data)):
          matrix[row_indices[i%len(row_indices)]][i]="*"
      dataindex=0
      for i in range(ke):
        for j in range(len(data)):
          if matrix[i][j]=="*":
            matrix[i][j]=data[dataindex]
            dataindex+=1

      dec=''
      for i in range(len(data)):
          dec+=matrix[row_indices[i%len(row_indices)]][i]

      print("Decrypted Text:",dec)
      with open("recover.txt", "w") as outfile:
          outfile.write(enc)
      print("Decrypted message stored in recover.txt")
    elif choice=='3':
      program=False
    else:
      print("Invalid choice. Please try again.")