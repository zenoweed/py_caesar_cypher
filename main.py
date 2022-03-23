# Python program for caesar cypher

def caesar(pt, key):
  ascii_val = ord(pt)
  add_key = ascii_val + key
  cipher = chr(add_key)
  print(cipher,end="")

k = 3
p = 'ARKHAM'

print ("Plaintext: ")
print (p)
print ("Cipertext: ")

i = len(p) # number of letters in word
a=0
while i != 0:
  letter = p[a]
  a+=1
  caesar(letter,k)
  i-=1