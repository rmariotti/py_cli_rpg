#!/usr/bin/env python3

class Item:
  def __init__(self, name="Item"):
    self.name = name
    
class Weapon(Item):
  def __init__(self, name="weapon", damage=0, rof=1, accuracy=1):
    Item.__init__(self, name)
    self.damage = damage
    self.rof = rof
    self.accuracy = accuracy