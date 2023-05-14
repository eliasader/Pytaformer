import pygame
from pygame.locals import *
#Import level / Importando a classe da platafoma
from platforms import World
#Import player class / Importando a classe do player
from player import Player
pygame.init()
#Creating the game window, FPS clock and window name / Criando a tela do jogo, o relogio de FPS 
# e o nome da janela 
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("The Golden Skull")        
#level map / mapa do nivel
worldData = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
#FPS variable / Variavel do FPS
FPS = 60
#Color variables / Variaveis de cor
windowColor = (100,100,100) 
#Gravity value / Valor da gravidade
GRAVITY = 1
#Creating world / Gerando o mundo
world = World(worldData,window)
#Creating player / Criando o player
player = Player(360,200,window,GRAVITY)
#Game loop and variable / Loop do jogo e sua variavel
going = True
while going:
    player.playerCollide(world.tileList)
    window.fill(windowColor)
    clock.tick(FPS)
#Player functions / Funções do player
    player.control_move()
    player.drawIt()
#Level funtions / Funções do nivel
    world.drawLevel()    
#Game quit loop / Loop de sair do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
            break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            going = False
            break
    pygame.display.flip()
pygame.quit()