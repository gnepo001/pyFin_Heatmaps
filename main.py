import pygame 
import sys
import math


#initalizes game 
class game():
    def __init__(self):
        pygame.init()
        self.WIDTH = 640
        self.HEIGHT = 640
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        #self.objs = {"AMZN":50,"GOOG":35,"SHOP":15,"tt":5}  
        self.objs = [50,35,15]  
        self.font = pygame.font.Font("freesansbold.ttf",32)
        self.tiles = HeatTiles(self.screen,self.objs)

    #main gameloop
    def run(self):
        
        while(True):
            l = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0,0,0))

            #renders through a bunch of force brute to get heat maps on the window
            self.tiles.draw()
            pygame.display.flip()

#Heat Tiles Initialize
class HeatTiles():
    def __init__(self,screen,marketCaps):
        self.marketCap = sum(marketCaps)
        self.screen = screen
        self.objPercentage = []
        self.objs = []
        
        x  = 0
        for i in marketCaps:
            percentage = i/self.marketCap
            self.objPercentage.append(percentage)
            map = HeatTile(self.screen,(0,255,0),x,0,50,50)
            self.objs.append(map)
            x +=50

    def draw(self):
        for i in self.objs:
            i.draw()

#individaul Heat Tile
class HeatTile():
    def __init__(self,screen,color,x,y,w,h):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.w,self.h))

if __name__ == "__main__":
    game = game()
    game.run()