#!/usr/bin/env python3

class Entity:
  def __init__(self, name="nome", hp=10, velocity=10, strength=10, intelligence=10, hand=None, items=[], lvl=1):
    from random import random
    self.name = name
    self.lvl = lvl
    self.hp = hp
    self.velocity = velocity + int(random()*10)
    self.strength = strength + int(random()*10)
    self.intelligence = intelligence + int(random()*10)
    self.hand = hand
    self.items = items
    
class Player(Entity):
  def __init__(self):
    Entity.__init__(self)
    self.name = str(input("What is your name?\n"))
    a = 1
    while a == 1:
      sure = input("Your name is: %s, are you sure?\n" % self.name)
      while sure not in ["no", "yes"]:
        sure = input("Your name is: %s, are you sure?\n" % self.name)
      if sure == "no":
        self.name = str(input("What is your name?\n"))
      else: a = 2
    classi = ("chemist", "developer", "engineer")
    alleanze = ("empire", "rebels")
    self.classe = str(input("Select your class (chemist|developer|engineer)\n"))
    while self.classe not in classi:
      self.classe = str(input("Choose your class (chemist|developer|engineer)\n"))
    self.alleanza = str(input("Choose your faction (empire|rebels)\n"))
    while self.alleanza not in alleanze:
      self.alleanza = str(input("Choose your faction(empire|rebels)\n"))