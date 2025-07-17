import random
from tkinter.font import Font
import pygame
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.const import *
            

        
            


class Level:
    def __init__(self, window, name, game_mode, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL
        if self.game_mode in (MENU_OPTION[1], MENU_OPTION[2]):
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self, player_score: list[int]):

        pygame.mixer_music.load('./assets/Level1.mp3')
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
                
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True
                    

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                
                if not found_player:
                    return False

    

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)