# typedis.py

'''
typedis
  compute & display score
  typing a-z
  set num of times in a round
'''
import random


letter = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'x', 't', 
 			'u', 'v', 'w', 's', 'y', 'z' ]



print("\nWelcome to Typedis!\n")

rounds = "invalid"

while not rounds.isdigit(): 
  rounds = input("Enter the number of rounds: ")
  print("Random int: ", random.randint(0,25))

rounds = int(rounds)
print("The number of rounds is: ", rounds)
print("The number of rounds is: ", rounds)



print("\nCya!\n")
