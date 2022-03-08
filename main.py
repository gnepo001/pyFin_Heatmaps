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
        self.objs = {"AMZN":50,"GOOG":35,"SHOP":15}  
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
        heatsquare = self.area * .5
        self.L = math.sqrt(heatsquare)
        self.W = math.sqrt(heatsquare)
        self.x2 = self.L
        heatsquare2 = self.area * .35
        self.L2 = math.sqrt(heatsquare2)
        self.W2 = math.sqrt(heatsquare2)
        if (self.L2*self.W2 + self.x2) >= self.WIDTH-10:
            self.W2 = self.WIDTH - self.x
            self.L2 = heatsquare2/self.W2
            print("bigger")

        #self.objs2 = {}
        
        

        # self.objs2 = {}
        # for i in self.objs:
        #         text = self.font.render(str(i),True,(0,255,0),(0,0,128))
        #         #textRect = pygame.draw.rect(self.screen,(255,0,0),(self.x,5,50,50))
        #         #self.screen.blit(text,(self.x,50))
        #         self.objs2.update({text:(self.x,50)})
        #         #print("inserted")
        #         self.x += 150

    #main gameloop
    def run(self):
        self.algo()
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0,0,0))
            text = pygame.draw.rect(self.screen,(255,0,0),(self.x,0,self.W,self.L))
            text2 = pygame.draw.rect(self.screen,(200,0,0),(self.x2,0,self.L2,self.W2))
            #self.screen.blit(self.text,(0,0))
            # for i,j in self.objs2.items():
            #     self.screen.blit(i,j)
            pygame.display.flip()

if __name__ == "__main__":
    game = game()
    game.run()