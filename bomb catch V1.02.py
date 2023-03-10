import sys, random, time, pygame
from pygame.locals import *
import winsound

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Bomb Catching Game")
font1 = pygame.font.Font(None, 24)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220, 50, 50
col = (230,230,50)
black = 0,0,0

lives = 3
score = 0
clock_start = 0
game_over = True
mouse_x = mouse_y = 0

pos_x = 300
pos_y = 460

bomb_x = random.randint(40,490)
bomb_y = -50
vel_y = 1.2

vel_x = 0.5

special = False
rando = False
s_ball = random.randint(1,8)

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
            
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0,0,0))

    if game_over:
        print_text(font1, 240, 250, "<CLICK TO PLAY>")
        print_text(font1, 90, 200, "<Left Arrow to move Left and Right Arrow to move Right>")
        vel_y = 0.1
    else:
        #move the bomb
        bomb_y += vel_y

        #has the player missed the bomb?
        if bomb_y > 500:
            bomb_x = random.randint(40, 490)
            bomb_y = -50
            lives -= 1
            
            special = False
            rando = False
            if lives == 0:
                game_over = True

        #see if player has caught the bomb
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                
                if special == True:
                    score+=30
                else:
                    score += 10
                vel_y=vel_y*1.02
                vel_x=vel_x*1.015
                winsound.Beep(70, 30)
                special = False
                rando = False
                bomb_x = random.randint(40, 490)
                bomb_y = -50
                
        if score >= 100:
            if rando == False:
                s_ball = random.randint(1,8)
                rando = True
                
            if s_ball == 1:
                special = True

        if special == True:
            col = (0, 200, 140)
        else:
            col = col = (230,230,50)
                    
                                        
        
        #draw the bomb
        pygame.draw.circle(screen, black, (bomb_x-4,int(bomb_y)-4), 30, 0)
        pygame.draw.circle(screen, col, (bomb_x,int(bomb_y)), 30, 0)

        #set basket position
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            pos_x+=vel_x
            
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            pos_x-=vel_x

        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500
            
        #draw basket
        pygame.draw.rect(screen, white, (pos_x,pos_y,120,40), 0)

    #print # of lives
    print_text(font1, 0, 0, "LIVES: " + str(lives))

    #print score
    print_text(font1, 500, 0, "SCORE: " + str(score))
    
    pygame.display.update()
