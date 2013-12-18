#!/us/bin/env python3
'''manage fight'''


class Fight:
    def __init__(self, entityOne, entityTwo):
        self.entityOne = entityOne
        self.entityTwo = entityTwo

    def faster(self):
        vel_ent1 = self.entityOne.velocity * self.entityOne.lvl
        vel_ent2 = self.entityTwo.velocity * self.entityTwo.lvl
        if vel_ent1 > vel_ent2:
            return self.entityOne, self.entityTwo
        elif vel_ent1 == vel_ent2:
            from random import choice
            ents = [self.entityTwo, self.entityOne]
            a = choice(ents)
            ents.remove(a)
            return a, ents[0]
        else:
            return self.entityTwo, self.entityOne

    def calculate_damage(self, player):
        try:
            dam = player.strength * player.lvl * player.hand.damage
        except:
            dam = player.strenght * player.lvl
        return dam

    def missed(self, player):
        from random import random
        try:
            accuracy = player.hand.accuracy * random()
        except:
            accuracy = 10 * random()
        if accuracy >= 3:
            return False
        else:
            return True

    def is_alive(self, player):
        if player.hp > 0:
            return True
        else:
            return False

    def fight(self):
        (frist, second) = self.faster()
        if self.missed(frist) is True:
            continue
        else:
            self.second.hp = self.second.hp - self.calculate_damage(frist)
        if self.is_alive(second) is True:
            if self.missed(second) is True:
                continue
            else:
                self.frist.hp = self.frist.hp - self.calculate_damage(second)
