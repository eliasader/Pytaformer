import pygame
from pygame.locals import *
#import time from python default library / Importar a função nativa "time" 
import time
class Player:
    playerVel = 3
    playerJump = -1.5
    def __init__(self,x,y,window,gravity):
        #Player image / Imagem do player
        self.img = pygame.image.load('img\player.png')
        #Generate image rect / Gerar retangulo apartir da imagem
        self.rect = self.img.get_rect()
        #Rect coordenates / Coordenadas do retangulo
        self.rect.x = x
        self.rect.y = y
        #How much the player is affected by gravity / O valor da gravidade
        self.gravity = gravity
        #The screen in which the player is in / Qual tela está o player
        self.window = window
        #Time the player has been falling / tempo em que o player esteve caindo
        self.time_fall = 0
        #Rect size variables / Variaveis do tamanho do retangulo
        self.width = self.img.get_width()
        self.height = self.img.get_height()
#Function to change position / Movimento da posição geral
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
#Draw object on window / "Desenhar" player na tela
    def drawIt(self):
        self.window.blit(self.img, self.rect)
#Gravity / Gravidade
    def playerGravity(self,didNotCollide):
        if didNotCollide:
            self.fall = self.time_fall/60 * self.gravity
            self.move(0,self.fall)
            self.time_fall += 5
        else:
            self.time_fall = 3
#Handle ALL player collisions / TODAS as colisões com o player
    def playerCollide(self,level):
        #Screen collision / Colisão com a tela
        if self.rect.bottom > 500:
            self.playerGravity(False)
        else:
            self.playerGravity(True)
        tolerance = 10
        #Platform collision / Colisão com a plataforma
        for tile in level:
            if tile[1].colliderect(self.rect):
                    if abs(self.rect.top - tile[1].bottom) < tolerance:
                        self.rect.top = tile[1].bottom
                    if abs(self.rect.bottom - tile[1].top) < tolerance:
                        self.playerGravity(False)
                        self.rect.bottom = tile[1].top    
                    if abs(self.rect.left - tile[1].right) < tolerance:
                        self.rect.left = tile[1].right
                    if abs(self.rect.right - tile[1].left) < tolerance:
                        self.rect.right= tile[1].left
#Handle player moviment / Controles de movimento do player
    def control_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.move(-self.playerVel,0)
        if keys[pygame.K_RIGHT] and self.rect.x + self.width < 500:
            self.move(self.playerVel,0)
        if keys[pygame.K_SPACE]:
            self.move(0,self.playerJump)