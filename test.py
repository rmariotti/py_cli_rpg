#!/usr/bin/env python3

import rooms
import entity

''' creazione delle stanze da creare durante il gioco '''

def rand_room(sub_rooms=1, name=1):
  room_list = []
  name_sub = name
  while sub_rooms > 0:
    name_sub = name_sub + 1
    sub_rooms = sub_rooms - 1
    room_list.append(rand_room(sub_rooms, name_sub))
  return rooms.Room(doors=room_list, description=("Door n°"+str(name)))

''' creazione di alcuni mostri '''

space_police = entity.Entity(name="space policeman",
			     hp=12, velocity=7,
			     strenght=7,
			     intelligence=2
			     hand=None
			     items=[]
			     lvl=1)