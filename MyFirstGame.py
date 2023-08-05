# OM NAMAH SHIVAY
# importing the pygame module to use
import pygame
import random
import sys
# import time
# Initialising the pygame module
pygame.init()
# sys.exit()
# Initialising the font
pygame.font.init()
# Creating an obstacle class
class obstacle:
    def __init__(self, bar1_x, bar1_width, bar1_height, bar2_x, bar2_width, bar2_height):
        self.bar1_x = bar1_x
        self.bar1_width = bar1_width
        self.bar1_height = bar1_height
        self.bar2_x = bar2_x
        self.bar2_width = bar2_width
        self.bar2_height = bar2_height   
    def create(self):
        global bar1
        bar1 = pygame.draw.rect(window, "red", pygame.Rect((bar1_x, bar_y), (bar1_width, 50)))
        global bar2
        bar2 = pygame.draw.rect(window, "red", pygame.Rect((bar2_x, bar_y), (bar2_width, 50)))
 
# Creating a clock
clock = pygame.time.Clock()
# # Setting a boolean variable
run = True
class JAI_MAHAKAAL:
    def __init__(self):
      pass
    def vars(self):
        global window, tit, score, scin, boat, inc, gap, bar_y, bar1_x, vec2, width, height, f, text, rec
        f = pygame.font.Font("freesansbold.ttf", 45)
        text = f.render("kgjl", False, "green", "black")
        rec = text.get_rect()
        rec.center = (300, 45)
        boat = pygame.image.load("boat3.png")
        # Setting display geometry
        width = pygame.display.get_desktop_sizes()[0][0]
        height = pygame.display.get_desktop_sizes()[0][1]

        window = pygame.display.set_mode((width, height-50))
        # Setting title
        tit = pygame.display.set_caption("My First Game")
        # Game variables and constants
        score = 0
        scin  = 1
        x = 0
        y = 0
        inc = 2
        gap = 50*4
        bar1_x = 0
        bar_y = 0
        vec2 = pygame.Vector2(x, y)
    def repobs1(self):
        global bar1_width
        bar1_width = random.randint(0, width-180)
        global bar2_x
        bar2_x = (bar1_width+gap)
        global bar2_width
        bar2_width = width - (bar1_width+gap)
    def norepobs1(self):
        pass
    def GameOver(self):
        f2 = pygame.font.Font("freesansbold.ttf", 90)
        text2 = f2.render('''Game Over''', False, "green", "black")
        rec2 = text2.get_rect()
        rec2.center = (250, 250)
        window.blit(text2, rec2)
        global scin
        scin = 0
        global inc
        inc = 0
        global gameover
        gameover = True
    def go(self):
        if bar_y == width-180 or vec2.x < bar1_width or vec2.x > bar2_width:
            global run
            run = False
    def repobs(self):
        global bar_y
        bar_y += inc
        global obst
        obst = obstacle(bar1_x, bar1_width, 50, bar2_x, bar2_width, 50)
        obst.create()
        if bar_y == height-180:
            if (bar1_width+40)>vec2.x or vec2.x>= bar2_x-40:
                # global run
                # run =  False
                self.GameOver()
                global f3
                f3 = pygame.font.Font("freesansbold.ttf", 20)
                text3 = f.render(f"Press R to continue......", False, "green", "black")
                rec3 = text.get_rect()
                rec.center = (360, 45)
                window.blit(text3, rec3)
    def maingame(self):
        # global run, gameover
        # run = True
        # gameover = False
        # global bar_y, score, obst
        # for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             run = False   
        # keys = pygame.key.get_pressed()
        #     # if keys[pygame.K_UP]:
        #         # y -= inc
        #     # if keys[pygame.K_DOWN]:
        #         # y += inc
        # if keys[pygame.K_LEFT]:
        #     vec2.x -= inc*8
        # if keys[pygame.K_RIGHT]:
        #     vec2.x += inc*8
        # if vec2.x > width-45:
        #     vec2.x = width-45
        # if vec2.x < 45 :
        #     vec2.x = 45
        # window.fill((68,238,255))
        # if self.repobs() == True:
        #     bar_y  = 0
        # # repobs1()
        # self.repobs()
        # if bar_y > height :
        #     bar_y = 0
        #     score+=scin
        #     self.repobs1()
        #     try:
        #         del obst
        #         # print(f"object deleted!")
        #     except:
        #         print("object not deleted")
        # self.repobs()
        # pg = pygame.transform.rotozoom(boat, -90, 0.3)
        # pgr =pg.get_rect()
        # pgr.center = (vec2.x, height-180)
        # window.blit(pg, pgr)
        # f = pygame.font.Font("freesansbold.ttf", 45)
        # text = f.render(f"Score: {score}", False, "green", "black")
        # rec = text.get_rect()
        # rec.center = (width-400, 20)
        # window.blit(text, rec)    
        # pygame.display.update()
        # clock.tick(60)
        # pygame.quit()
        # quit()
        pass
    def mainloop(self):
        global run, gameover
        run = True
        gameover = False
        global bar_y, score, obst
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False   
            keys = pygame.key.get_pressed()
                # if keys[pygame.K_UP]:
                    # y -= inc
                # if keys[pygame.K_DOWN]:
                    # y += inc
            if keys[pygame.K_LEFT]:
                vec2.x -= inc*8
            if keys[pygame.K_RIGHT]:
                vec2.x += inc*8
            if vec2.x > width-45:
                vec2.x = width-45
            if vec2.x < 45 :
                vec2.x = 45
            window.fill((68,238,255))
            if self.repobs() == True:
                bar_y  = 0
            # repobs1()
            self.repobs()
            if bar_y > height :
                bar_y = 0
                score+=scin
                self.repobs1()
                try:
                    del obst
                    # print(f"object deleted!")
                except:
                    print("object not deleted")
            self.repobs()
            pg = pygame.transform.rotozoom(boat, -90, 0.3)
            pgr =pg.get_rect()
            pgr.center = (vec2.x, height-180)
            window.blit(pg, pgr)
            f = pygame.font.Font("freesansbold.ttf", 45)
            text = f.render(f"Score: {score}", False, "green", "black")
            rec = text.get_rect()
            rec.center = (width-400, 20)
            window.blit(text, rec)    
            pygame.display.update()
            clock.tick(60)
        pygame.quit()
        # quit()
Game = JAI_MAHAKAAL()
Game.vars()
Game.repobs1()
Game.repobs()
Game.maingame()
Game.mainloop()