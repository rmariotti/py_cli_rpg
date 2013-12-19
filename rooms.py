#!/usr/bin/env python3
''' class that create rooms '''


class Room:
    def __init__(self, items=[], doors=[], entities=[], description="",
                 is_locked=False):
        self.items = items
        self.doors = doors
        self.entities = entities
        self.description = description

    def create_subdoor(self, items=[], doors=[] entities=[], description="",
                       is_locked=False):
        doors.append(self)
        a = self.__init__(items, doors, entities, description is_locked)
        return a
