import random
from tkinter.font import Font
import pygame
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, ENEMY_SPAWN, C_GREEN, C_CYAN
            

        
            


class Level2:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level2Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000
        if self.game_mode in (MENU_OPTION[1], MENU_OPTION[2]):
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN)


    def run(self):

        pygame.mixer_music.load('./assets/Level2.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:

            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                
                if ent.name == 'Player1':
                    self.level_text(20, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (101, 20))
                if ent.name == 'Player2':
                    self.level_text(20, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (101, 35))


            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (80, 5))
            self.level_text(20, f'fps: {clock.get_fps():.0f}', C_WHITE, (30, WIN_HEIGHT - 35))
            self.level_text(20, f'entidades: {len(self.entity_list)}', C_WHITE, (50, WIN_HEIGHT - 20))

            pygame.display.flip()

            EntityMediator.verify_colision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

    

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)