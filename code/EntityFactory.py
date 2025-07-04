from code.Background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Enemy import Enemy
import random



class EntityFactory:


    def get_entity(entity_name, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', position=(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH,0)))
                return list_bg
            
            case 'Player1':
                return Player('Player1', (30, WIN_HEIGHT / 2 - 20))
            
            case 'Player2':
                return Player('Player2', (30, WIN_HEIGHT / 2 + 20))
            
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            
             
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            