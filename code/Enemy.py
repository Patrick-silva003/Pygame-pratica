from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.const import *


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]


    
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
      
    
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(f'{self.name}Shot', (self.rect.centerx, self.rect.centery))