import numpy as np

print("Welcome to the Columnar Transposition Cipher.")
print("What do you wish to do?")
program=True
while program:
    print("1. Encryption")
    print("2. Decryption")
    print("3. End Program")
    choice = input("Enter your choice: ")
    if choice == "1":
      f = "file.txt"
      ke = input("Enter the cipher key: ")
      keylist=[]
      
      for i in ke:
        keylist.append(i)
      sortedkey=sorted(keylist)
      dic={}
      for key in range(len(sortedkey)):
        dic[sortedkey[key]]=str(key+1)
      for key in ke:
        ke=ke.replace(key,dic[key])


      with open(f, "r") as infile:
          data = infile.read()
      rows=len(data)/len(ke)
      if rows>rows//1:
        rows=int(rows//1+1)
      else:
        rows=int(rows//1)
      enc=''
      index=0
      matrix=[['']*len(ke) for i in range(rows)]
      for i in range(rows):
        for j in range(len(ke)):
          if index<len(data):
            matrix[i][j]=data[index]
          index+=1
      for col in ke:
        col=int(col)-1
        for row in range(rows):
          if matrix[row][col]!='':
            enc+=matrix[row][col]
      print("Encrypted Text:",enc)
      with open("cipher.txt", "w") as outfile:
          outfile.write(enc)
      print("Encrypted message stored in cipher.txt")
    elif choice=='2':
      f = "cipher.txt"
      ke = input("Enter the cipher key: ")
      keylist=[]
      for i in ke:
        keylist.append(i)
      sortedkey=sorted(keylist)
      dic={}
      for key in range(len(sortedkey)):
        dic[sortedkey[key]]=str(key+1)
      for key in ke:
        ke=ke.replace(key,dic[key])

      with open(f, "r") as infile:
          data = infile.read()

      rows=len(data)/len(ke)
      if rows>rows//1:
        rows=int(rows//1+1)
      else:
        rows=int(rows//1)

      lastcol=len(data)%len(ke)
      d={}
      for i in range(len(ke)):
        d[i]=rows
      for i in range(lastcol,len(ke)):
        d[i]-=1
      print(d)
      dec=''
      matrix=[['']*len(ke) for i in range(rows)]
      index=0
      for col in ke:
        col=int(col)-1
        for row in range(d[col]):
          matrix[row][col]=data[index]
          index+=1
      for row in range(rows):
        for col in range(len(ke)):
          dec+=matrix[row][col]

      print("Decrypted Text:",dec)
      with open("recover.txt", "w") as outfile:
          outfile.write(dec)
      print("Decrypted message stored in recover.txt")
    elif choice=='3':
      program=False
    else:
      print("Invalid choice. Please try again.")
