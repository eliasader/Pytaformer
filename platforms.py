import pygame
from pygame.locals import *
#tile size var
tileSize = 50
class World:
    def __init__(self,data,window):
        #actual world data
        self.tileList = []
        #loading images
        self.floorImg = pygame.image.load('img\\floor.png')
        self.window = window
        #generate world structure
        rowCount = 0
        for row in data:
            tileCount = 0
            for tile in row:
                if tile == 1:
                    imgRect = self.floorImg.get_rect()
                    imgRect.x = tileCount * tileSize
                    imgRect.y = rowCount * tileSize
                    tile = (self.floorImg,imgRect)
                    self.tileList.append(tile)
                tileCount += 1
            rowCount += 1        
    def drawLevel(self):
        for tile in self.tileList:
            self.window.blit(tile[0],tile[1])