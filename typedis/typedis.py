# typedis.py

'''
typedis
  compute & display score
  typing a-z
  set num of times in a round
'''
import random



def randWord( rounds ):
  for i in range(rounds):
  	question = letter[random.randint(0,25)]
  	yield question
  	


letter = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'x', 't', 
 			'u', 'v', 'w', 's', 'y', 'z' ]

rounds = "invalid"
score = 0
size = 3

print("\nWelcome to Typedis!\n")



# while not rounds.isdigit():  # loop until a num is entered
#   rounds = input("Enter the number of rounds: ")

rounds = 5
rounds = int(rounds)
print("The number of rounds is: ", rounds)


# 1 question per rounds
for i in range(rounds):
  print("\nRound ", i+1, ":")
  

  question = letter[random.randint(0,25)]


  print(question)
  answer = input()
  if answer == question:
  	score += 1


print("\nYour score is: ", score)
print("\nCya!\n")
