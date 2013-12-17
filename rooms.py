#!/usr/bin/env python3

class Room:
  def __init__(self, items=[], doors=[], entities=[], description=""):
    self.items = items
    self.doors = doors
    self.entities = entities
    self.description = description