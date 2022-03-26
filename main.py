# Python program for caesar cypher

k = 3
a = 0
p = 'THE QUICK FOX JUMPED OVER THE LAZY BROWN DOG'
i = len(p) # number of letters in word

def enCaesar(pt, key):
  if pt == " ":
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


print ("Plaintext: ")
print (p)
l=1
while l != 0:
  choice = int(input("""\n\n  Choose:
         1. Encipher
         2. Decypher
  
    Input: """))
  
  print ("Cipertext: ",)
  while i != 0:
    letter = p[a]
    a += 1
    if choice == 1:
      enCaesar(letter,k)
    elif choice == 2:
      deCaesar(letter,k)
    else:
      print ("Invalid. Try again")
    i-=1