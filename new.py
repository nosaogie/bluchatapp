import random


nam = input("what is your name")
print("welcome",nam)
another=input("what do you want to do\nA-a football quiz\nB-a guesser game")
def no():
  print("welcome to the guesser game")
  game =  input("guess the number") 
  if game.isdigit():
    game = int(game)

    if game <= 0:
        print("whatever you want to print")
        quit()
  else:
    quit()

  randy = random.randint(0, game)
  num=0

  while True:
    num += 1
    new = input("make a guess")
    if new.isdigit():
        new = int(new)
    else:
        print ( "type a number next time")  
        continue
    if new == randy:
        print("correct")
        break
    elif new > randy:
        print("close boiiiiiiiii")
    else:
        print("close boiiiiii")
  print("you had ", num ,"guesses")

def yo():
       score=0
       print("welcome to the football quiz game")
       gavi = input("do you play football")
       if gavi.lower() !="yes":
        print("closing the game")
        quit()

       print("do yer stuff")
       score=0

       ball = input("who is the G.O.A.T")
       if ball.lower() == "messi":
        print("correct")
        score +=1
       else:
        print("you idiot you looooooooose")
        quit()

       q2 = input("wha is the best club")
       if q2.lower() == "fc barcelona":
         print("correct")
         score +=1
       else:
         print("you idiot you looooooooose")
         quit()

       q3 = input("who is the best goal keeper")
       if q3.lower() == "courtois":
         print("correct")
         score +=1
       else:
         print("you idiot you looooooooose")
         quit()

if another.upper() =="A" :
    yo() 

elif another.upper() =="B":
  no()
