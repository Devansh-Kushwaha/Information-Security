import random
from sympy import isprime

def isPrime(n):
  return isprime(n)
def gcd(i,j):
  r=j%i
  q=j//i
  if r==0:
    return i
  else:
    return gcd(r,i)
def modInverse(e,n,t1=0,t2=1):
  r=n%e
  q=n//e
  t=t1-(t2*q)
  if r==0:
    return t2
  else:
    return modInverse(r,e,t2,t)

def binary_exponentiation(base,exponent,modulus):
  result=1
  base=base%modulus
  while exponent>0:
    if exponent%2==1:
      result=(result*base)%modulus
      exponent-=1
    else:
      base=(base*base)%modulus
      exponent//=2
  return result%modulus


def generate_1024_bit_prime():
  while True:
    number=random.getrandbits(1024)|1
    if isPrime(number):
      return number


message=int(input("Enter a message: "))


p=generate_1024_bit_prime()
q=generate_1024_bit_prime()

n=p*q
phi=(p-1)*(q-1)

if n<message:
  try:
    p=generate_1024_bit_prime()
    q=generate_1024_bit_prime()
    n=(p-1)*(q-1)
  except:
    message=int(input("Enter a message in range 1 to"+n-1))



#choosing e
e=65537
while gcd(e, phi) != 1:
    e = random.randrange(2, phi)

d=modInverse(e,phi,0,1)%phi

cipher=binary_exponentiation(message,e,n)

decipher=binary_exponentiation(cipher,d,n)

print("Encrypted Message:",cipher)
print("Decrypted Message:",decipher)