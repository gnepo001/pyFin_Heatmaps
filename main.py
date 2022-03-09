import pygame 
import sys
import math

### force brutes to getting some percentage base heat maps less than 5 on the window

#initalizes game 
class game():
    def __init__(self):
        pygame.init()
        self.WIDTH = 640
        self.HEIGHT = 640
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.objs = {"AMZN":50,"GOOG":35,"SHOP":15,"tt":5}  
        self.font = pygame.font.Font("freesansbold.ttf",32)
        
    def algo(self):
        self.area = self.WIDTH * self.HEIGHT
        self.totalMarketCap = 0
        self.objPercentage = {}
        for i,k in self.objs.items():
            self.totalMarketCap += k
        for i,k in self.objs.items():
            percentage = k/self.totalMarketCap
            self.objPercentage.update({i:percentage})
        #print(self.objPercentage)
        self.x = 0
        self.objs3 = {}
        if len(self.objs) <= 5:
            for i, k in self.objPercentage.items():
                length = k * self.WIDTH
                self.objs3.update({length:self.HEIGHT})
  
    #main gameloop
    def run(self):
        self.algo()
        while(True):
            l = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0,0,0))

            #renders through a bunch of force brute to get heat maps on the window
            tt= 0
            temp = 0
            for i,j in self.objs3.items():
                pygame.draw.rect(self.screen,(255,tt+10,0),(self.x+temp,0,i,j))
                temp += i
                tt+=50
            pygame.display.flip()

if __name__ == "__main__":
    game = game()
    game.run()