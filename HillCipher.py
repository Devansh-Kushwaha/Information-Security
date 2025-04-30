import numpy as np

print("Welcome to the Hill Cipher.")
print("What do you wish to do?")
program=True
while program:
    print("1. Encryption")
    print("2. Decryption")
    print("3. End Program")
    choice = input("Enter your choice: ")
    if choice == "1":
        # data=input("Enter the input: ")
        data="ATTACK"
        # key = input("Enter the cipher key: ")
        key = "CDDG"
        rootkey=len(key)**(1/2)
        if rootkey//1==rootkey:
          rootkey=int(rootkey)
        else:
          rootkey=int(rootkey)+1
        keymatrix=[['']*rootkey for _ in range(rootkey)]
        count=0
        for i in range(rootkey):
          for j in range(rootkey):
            if count<len(key):
              keymatrix[i][j]=ord(key[count])-ord('A')
              count+=1
            else:
              keymatrix[i][j]=ord('X')-ord('A')
        pairs=[]
        for i in range(0,len(data),rootkey):
          temp=[]
          for j in range(i,i+rootkey):
            if j<len(data):
              temp.append(ord(data[j])-ord('A'))
            else:
              temp.append(ord('X')-ord('A'))
          pairs.append(temp)
          print(temp)
        products=[]
        
        keymatrix=np.array(keymatrix)
        for pair in pairs:
          pair=np.array(pair)
          mul=np.dot(keymatrix,pair)
          products.append(mul)
        enc=""
        for product in products:
          for num in product:
            num=num%26
            enc+=chr(num+ord('A'))
        print("Encrypted Text:",enc)
        with open("cipher.txt", "w") as outfile:
            outfile.write(enc)
        print("Encrypted message stored in cipher.txt")


    elif choice=='2':
      f = "cipher.txt"
      with open(f, "r") as infile:
          data = infile.read()
      ke =input("Enter the cipher key: ")
      rootkey=len(key)**(1/2)
      if rootkey//1==rootkey:
        rootkey=int(rootkey)
      else:
        rootkey=int(rootkey)+1
      keymatrix=[['']*rootkey for _ in range(rootkey)]
      count=0
      for i in range(rootkey):
        for j in range(rootkey):
          if count<len(key):
            keymatrix[i][j]=ord(key[count])-ord('A')
            count+=1
          else:
            keymatrix[i][j]=ord('X')-ord('A')

      keyadjoint=np.linalg.inv(np.array(keymatrix))*np.linalg.det(keymatrix)

      from sympy import mod_inverse

      inversedeterminant=mod_inverse(int(np.linalg.det(keymatrix))%26,26)
      keyadjoint=keyadjoint*inversedeterminant
      keyinverse=keyadjoint%26

      pairs=[]
      for i in range(0,len(data),rootkey):
        temp=[]
        for j in range(i,i+rootkey):
          if j<len(data):
            temp.append(ord(data[j])-ord('A'))
          else:
            temp.append(ord('X')-ord('A'))
        pairs.append(temp)


      products=[]

      for pair in pairs:
        pair=np.array(pair)
        mul=np.dot(keyinverse,pair)
        products.append(mul)

      dec=""
      for product in products:
        for num in product:

          num=int(np.round(num))%26

          dec+=chr(int(num)+ord('A'))


      for i in range(len(dec)-1,-1,-1):
        if dec[i]!='X':
          dec=dec[:i+1]
          break
      
      print("Decrypted Text:",dec)
      with open("recover.txt", "w") as outfile:
          outfile.write(enc)
      print("Decrypted message stored in recover.txt")

    elif choice=='3':
      program=False
    else:
      print("Invalid choice. Please try again.")
