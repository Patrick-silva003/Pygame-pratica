from code.Entity import Entity
from code.const import *


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)


    
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH