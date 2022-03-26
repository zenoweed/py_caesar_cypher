# Python program for caesar cypher

k = 3
p = 'THE QUICK FOX JUMPED OVER THE LAZY BROWN DOG'
i = len(p) # number of letters in word

def enCaesar(pt, key):
  if pt == " ":
    print(pt, end="")
  else:
    ascii_val = ord(pt)
    #print("ASCII VAL of "+ pt + ": ",ascii_val)
    add_key = ascii_val + key
    #print("ASCII VAL + key of "+ pt + ": ",add_key)
    if add_key > 90:
      mod = add_key - 90
      add_key = 64 + mod
      
    cipher = chr(add_key)
    print(cipher,end="")

def deCaesar(pt, key):
  if pt == " ":
    print(pt, end="")
  else:
    ascii_val = ord(pt)
    #print("ASCII VAL of "+ pt + ": ",ascii_val)
    add_key = ascii_val + key
    #print("ASCII VAL + key of "+ pt + ": ",add_key)
    if add_key > 90:
      mod = add_key - 90
      add_key = 64 + mod
      
    cipher = chr(add_key)
    print(cipher,end="")

print ("Plaintext: ")
print (p)


choice = input("""  Choose:
       1. Encipher
       2. Decypher

  Input: """)

print ("Cipertext: ",)
while i != 0:
  a = 0
  letter = p[a]
  a += 1
  #if choice == 1:
  enCaesar(letter,k)
  #else:
    #deCaesar(letter,k)
  i-=1