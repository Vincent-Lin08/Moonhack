#!/bin/python3
import random
events = [
  ("You are beginning to smell, do you take a shower?",-200,0),
  ("You hear a hissing sound, do you investigate?",-100,-500),
  ("A lump of ice has fallen from the sky nearby, do you retrieve it?",100,-50),
  ("You watched a YouTube video about the best lawns in the solar system. Do you decide to try and grow a lawn in the desolate Martian soils?", -300, 0),
  ("Your cousin Harold has mysteriously appeared. Do you send him away?", -50, -200),
  ("Mmm, salty food. Do you eat it?", -3, 0),
  ("You spot an oasis off in the distance, do you investigate?", -20, 0),
  ]
  
water = 1000
day = 1 

while water > 0:
  water -= 5
  print ("A day has passed. Your water " + str(water) + "L")
  event = random.choice(events)
  while True:
    response = input(event[0] + " (yes/no): ")
    if response == "yes":
      water += event[1]
      break
    elif response == "no":
      water += event[2]
      break
    else:
      ("input yes or no")
    
  day += 1
  
print ("Game over idiot you lasted " + str(day) + " days")