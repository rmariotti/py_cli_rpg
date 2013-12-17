#!/usr/bin/env python3

import entity
import items
import command
import spazzatura

class Game:
  def __init__(self):
    self.player = entity.Player()
    self.room = spazzatura.rand_room(3)
 
  def pick_item(self, item):
    self.player.items.appen(item)
    
  def take_in_hand(self, item):
    self.player.hand = item
    
  def kick(self, args):
    self.player.hp = self.player.hp - 1
  
  def examine(self, args):
    print(self.room.description)
    
  def print_doors(self, args):
    for i in range(len(self.room.doors)):
      print(self.room.doors[i].description)
    
  def open_door(self, door):
    for i in range(len(self.room.doors)):
      if door == self.room.doors[i].description:
        self.prec_room = self.room
        self.room = self.room.doors[i]
        return True
    print("No door found")

  def print_stats(self, args):
    print(self.player.name +
	  ' lvl.' + str(self.player.lvl) +
	  ' ' + self.player.classe + ' ' +self.player.alleanza +
	  '\nintelligence: ' + str(self.player.intelligence) +
	  '\nstrength: ' + str(self.player.strength) +
	  '\nvelocity: ' + str(self.player.velocity))

if __name__ == "__main__":
  gioco = Game()
  commands = {'kick':gioco.kick,
	      'examine':gioco.examine,
	      'doors': gioco.print_doors,
	      'open': gioco.open_door,
	      'stats': gioco.print_stats} 
  cli = command.Command(prompt=">>> ", intro="PyRpgCli", logout="See you!", command_list=commands)
  a = True
  while a == True and gioco.player.hp > 0:
    a = cli.do()
  print("You're death the %s lost" % gioco.player.alleanza)