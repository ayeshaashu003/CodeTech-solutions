import time
import pygame

pygame.init()
pygame.mixer.init()

def chapter1(playersChoice):
    time.sleep(0.5)
    if playersChoice == "start":
      print("\n")
      print("CHAPTER-1")
      print("Virtual World\n")
      print("It's 2095, a new Virtual Reality Game has been launched. There's Hype everywhere.\n")
      print("Do you like to play or skip?\nEnter y/n")
      playersChoice=input().lower()
      if(playersChoice=="y"):
          print("\nYou turn your PC on and put on your NERVE GEAR to enter the virtual world.")
          for i in range(3,0,-1):
            time.sleep(1)
            print(i)
          print("\nWelcome to \"SWORD ART ONLINE\"")
          chapter2()
      elif(playersChoice=='n'):
        print("\nYou remain idle and couldn't have fun and you regret.")
        time.sleep(0.5)
        print("wanna go again? y/n")
        goagain = input()
        if(goagain== 'y'):
           chapter1("start")
        elif(goagain=='n'):
           pass
    else:
        print("\nWrong input, press `start` to play")


def chapter2():
   time.sleep(0.5)
   print("\nCHAPTER-2: Roam around the arena.")
   print("\nYou have been spawned in the arena, where all players gather.")
   print("A girl named Asuna wants to have a chat with you.")
   print("ASUNA: `Hey there!`")
   print("\nWhat do you want to do?:(enter a number)")
   print("1. Chat with her.")
   time.sleep(0.5)
   print("2. Ignore her.")
   decision1= input()
   if(decision1 =="1"):
      print("\nYOU: `Hello. Nice to meet you.`")
      print("ASUNA: `It seems you are a new player, BTW I'm a Beta Tester. I can show you around.`")
      print("What do you want to do?")
      print("1. Let's go.")
      time.sleep(0.5)
      print("2. I hate Beta Testers.")
      decision2 =input()
      if(decision2=="1"):
         print("\nASUNA: `Yey! It'll be fun`")
         chapter3()
      elif(decision2=="2"):
         print("\nASUNA:`That's so rude`")
         print("Asuna walks away!...")
         print("wanna go again? y/n")
         goagain = input()
         if(goagain== 'y'):
           chapter2()
         elif(goagain=='n'):
           pass
   elif(decision1=="2"):
      time.sleep(0.5)
      print("\nYou Ignore her and moves to other place.")
      print("wanna go again? y/n")
      goagain = input()
      if(goagain== 'y'):
           chapter2()
      elif(goagain=='n'):
           pass
 

def chapter3():
   time.sleep(0.5)
   print("\nCHAPTER-3: The Dungeon.")
   print("\nWhile, travelling across the arena, you guys found a Great Dungeon which is very large and looks so dark.")
   print("ASUNA: `Shall we enter, may be we can have our first fight to clear the stage?`")
   print("What do you want to do?")
   print("1. No I can't go in, I'm so scared")
   time.sleep(0.5)
   print("2. Yeah! Let's go in")
   decision3= input()
   if(decision3=="1"):
      print("ASUNA: `You are such a coward, Hahaha.")
      chapter4()
   elif(decision3=="2"):
      print("ASUNA: `That's so Brave, let's get ready for the upcomings.")
      print("YOU:` Yeah!`")
      print("Both enters into the dungeon and takes their swords out to fight.")
      print("Suddenly a sound is heard.")
      time.sleep(0.5)
      sound_effect_path ='C:\INTERNSHIP\TASK-1(adventure game)\mixkit-aggressive-monster-beast-roar-14 (1).wav';
      play_sound(sound_effect_path)
      print("\nYou both get scared of it and looks around for trouble.")
      chapter4_5()



      
def chapter4():
   time.sleep(0.5)
   print("\nYou both exit the Dungeon and goes to another place where there are lots of people.")
   chapter5()

def chapter4_5():
   time.sleep(0.5)
   print("\nCHAPTER-4: Fight with the Beast")
   print("\nYou find yourselves a new player, named `Yuki` who entered the dungeon before you")
   print("The monster named `stone-hammer` appears with a 15000HP. ")
   print("You three use your sword skills and defeat the monster")
   time.sleep(0.5)
   print("\nYou three return back to arena")
   chapter5()
   

def chapter5():
   time.sleep(0.5)
   print("\nAkiho, the maker of the game, appears in-game")
   print("\nAKIHO:`Welcome to SAO, where you can have a MMORPG styled virtual experience.")
   time.sleep(0.5)
   print("\nAnd the twist is you guys are stuck here and can't go back to the real world unlesss you clear the game.")
   print("All scatter and tries to run here and there.")
   final()

def final():
   time.sleep(0.5)
   print("\nNow, you woke up on your bed and now that was a dream.")



def play_sound(file_path):
   try:
      sound_eff = pygame.mixer.Sound(file_path)
      sound_eff.play()

      pygame.time.wait(int(sound_eff.get_length()*1000))
   
   except pygame.error as e:
      print(f"Error:{e}")
   finally:
      pygame.quit()



print("Enter \"start\" to play")
playersChoice= input().lower()

chapter1(playersChoice)


