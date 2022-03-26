# Python program for caesar cypher

k = 3
a = 0
#p = 'THE QUICK FOX JUMPED OVER THE LAZY BROWN DOG'
p = 'A B C X Y Z'
i = len(p) # number of letters in word

def deCaesar(pt, key):
  if pt == " ":
    print(pt, end="")
  else:
    ascii_val = ord(pt)
    print("ASCII VAL of "+ pt + ": ",ascii_val)
    add_key = ascii_val - key
    print("ASCII VAL - key of "+ pt + ": ",add_key)
    if add_key < 65:
      mod =  65 - add_key
      print(mod)
      add_key = 91 - mod
      
    cipher = chr(add_key)
    print("C: ")
    print(cipher)#,end="")

print ("Plaintext: ")
print (p)


#choice = input("""  Choose:
 ##     2. Decypher
#
 # Input: """) 

print ("Cipertext: ",)
while i != 0:
  letter = p[a]
  print("Letter: ",letter)
  a += 1
  deCaesar(letter,k)
  i-=1