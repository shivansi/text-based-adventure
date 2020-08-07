print("Welcome to: THE LEAGUE OF VILLAINS ATTACK!!")
print("(characters are from My Hero Academia)")

options=["A","B","C"]

name = input("hello, what is your name? \n")


print(f"hello {name}! Let's start the adventure.")

def start():
  print("It's a beautiful sunny summer day but then you hear a loud ")


  for i in range(3):
    print("BOOM")
  print("what's that noise? you look outside of your window and see 10 nomus wreaking havoc onto your city. One spots you!!!")

  answer=input("What do you do?! choose A , B , or C. \nA) Run away! \nB) Gather many kitchen knives to try and fight the nomus \nC) Check if anyone is saying anything about it on Twitter \n")

  while answer not in options:
    print("not a valid option. please answer a, b, or c")
    answer=input("What do you do?! choose A , B , or C. \nA) Run away! \nB) Gather many kitchen knives to try and fight the nomus \nC) Check if anyone is saying anything about it on Twitter \n")
  answer_options(answer)

def answer_runAway():
  print("You run out and then find a tall man right infront of you. You think he is a good guy so you hug him and ask what is going on. He laughs like a maniac. That's when you knew that he was not a good guy. Infact, that is SHIGARAKI!!! THE LEADER OF THE LEAGUE OF VILLAINS!!! You slowly step back, scared for your life! He uses his quirk and dissintegrates your body. He laughs like a maniac and leaves your corpse there...YOU DIED!!!")


def answer_attackNomus():
  print("All ten of the Nomus come towards you. You try piercing them with your knives but you clearly underestimated their strength. They doged them so easily!!! They all come towards you with a shriek! And the next thing you know is that you are being ripped apart slowly by the nomus. They want you to feel the pain. You didn't even get to say goodbye...")

def answer_checkTwt():
  print("You check Twitter, only to find out that you have no wifi! You are confused because your wifi is always good... You look outside to see that the nomus are destroying the signal tower! That's why the wifi was dead... You decide to take matters into your own hands and try to fix the tower yourself, since you are very good at fixing things. You snuck past the nomus and went to the tower easily. What you didnt know was that there was someone watching you. While you were fixing the tower, you heard growls... You turned around to see SORAMITSU TABE!!! You heard that he eats anything and that he has really strong teeth. You were scared so you tried to head down the tower slowly. Tabe didn't want you to leave... So he bit your head off in an instant...GAME OVER :) ")
def answer_options(answer):
  if answer.upper()=="A":
    print(answer_runAway)
    answer_runAway()
  elif answer.upper()=="C":
    print(answer_checkTwt)
    answer_checkTwt()
  elif answer.upper()=="B":
    print(answer_attackNomus)
    answer_attackNomus()
  else:
    print("try again, choose a,b,or c")
    start()


def main():
  start()

main()
