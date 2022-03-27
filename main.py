# Python program for caesar cypher

k = 3 # key of cipher
a = 0 # start of array
p = 'THE QUICK FOX JUMPED OVER THE LAZY BROWN DOG' # plaintext
i = len(p) # number of letters in word
choice = 0 # choice of encryption or decryption

def enCaesar(pt, key):
  if pt == " ": # checks for spaces and returns em without any change
    print(pt, end="")
  else:
    ascii_val = ord(pt)
    add_key = ascii_val + key
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
    add_key = ascii_val - key
    if add_key < 65:
      mod =  65 - add_key
      add_key = 91 - mod
      
    cipher = chr(add_key)
    print(cipher,end="")
  
choice = int(input("""\n\n==========================================
                   
                   Choose:
       1. Encipher
       2. Decypher

  Input: """))

print ("  Choice: ", choice)
print ("  Plaintext:",p,end="")
print ("\n  Cipertext: ",end="")

while a != i:
  letter = p[a]
  a += 1
  if choice == 1:
    enCaesar(letter,k)
  elif choice == 2:
    deCaesar(letter,k)
  else:
    print ("INVALID")

print ("\n")