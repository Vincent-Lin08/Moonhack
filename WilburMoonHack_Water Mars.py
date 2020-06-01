#!/bin/python3
import random
playing = True
while playing == True:
  events = [
    ("You are beginning to smell, do you not want to take a shower?",-100 ,0, -30),
    ("You hear a hissing sound, do you investigate?", 0, 0, -10),
    ("A lump of ice has fallen from the sky nearby, do you retrieve it?",100,-50, -10),
    ("You watched a YouTube video about the best lawns in the solar system. Do you decide to try and grow a lawn in the desolate Martian soils?", -300, 0, -30),
    ("Your dirty cousin Harold has is visiting. Do you let him stay?", -50, -200, -20),
    ("Mmm, salty food. Do you eat it?", -3, 0, -10),
    ("You spot an oasis off in the distance, do you investigate?", -20, 0, -30),
    ("You're hands are getting dirty, do you not want to wash them?", -30, 0, -5),
    ("Your plants are getting dry, would you want to water them?", -20, 0, -5),
    ("Your teeth are getting dirty, would you not want to brush them?", -20, 0, -10),
    ]
  dieclean = False
  use = 5
  clean = 100
  day = 1
  water = 1000
  alive = True
  while water > 0:
    water = water - use
    day += 1
    print("Day " + str(day) + ". Your Water " + str(water) + " Liters. " + "Your cleaness is " + str(clean))
    event = random.choice(events)
    while alive == True:
      if clean < 1:
        alive = False
        water = 0
        dieclean = True
      if dieclean == False:
        response = input(event[0] + "(yes/no)").lower()
        if response == "yes":
          water += event[1]
          clean += event[3]
          break
        elif response == "no":
          water += event[2]
          
          break
        else:
          print("Please answer yes or no!!!!")
     

      
  if dieclean == True:
    print("You lasted " + str(day) + " days. " + "You died of diarrhoea!!!!!" + " YOU ARE SO DIRTY!!!!!!!")
  else:
    print("You lasted " + str(day) + " days. " + "Your cleaness is " + str(clean))
  
    
  play = input("Do you want to play again? (yes/no)").lower
  if play == "yes":
    playing = True
  else:
    playing = False
