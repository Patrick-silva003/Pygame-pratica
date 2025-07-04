import pygame


C_WHITE = (255, 255, 255)
C_ORANGE = (255, 165, 0)
C_YELLOW = (255, 255, 0)

EVENT_ENEMY = pygame.USEREVENT + 1

ENEMY_SPAWN = 3000

MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'NEW GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT'
)

PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}

PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}

PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}

PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}



ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60
}






ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0.5,
    'Level1Bg2': 1,
    'Level1Bg3': 1.5,
    'Level1Bg4': 2,
    'Level1Bg5': 2.5,
    'Level1Bg6': 3,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 1.5,
    'Enemy2': 2
}

WIN_WIDTH = 573
WIN_HEIGHT = 324

