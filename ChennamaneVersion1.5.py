import random, pygame, sys
from pil import gui
import win32api
import win32gui
import win32con
import win32com.client
import turtle
import locale
from ctypes import *


import time
import math

from pygame.locals import *
import ctypes

# set mouse events
MOUSEEVENTF_MOVE = 0x0001 # mouse move
MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move
MOUSEEVENTF_MOVEABS = MOUSEEVENTF_MOVE + MOUSEEVENTF_ABSOLUTE

MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down 
MOUSEEVENTF_LEFTUP = 0x0004 # left button up 
MOUSEEVENTF_CLICK = MOUSEEVENTF_LEFTDOWN + MOUSEEVENTF_LEFTUP




# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
OLIVE = (128, 128, 0)
GRAY = (128, 128, 128)
FUCHISA = (255, 0, 255)
LIME = ( 0, 255, 0)

#Global Variables
Player1 = 0
Player2 = 0
User1 = False
User2 = False


# Player1V1 -> Player1V2 -> Player1V3 -> Player1V4 -> Player1V5 -> Player2V5
#  -> Player2V4 -> Player2V3 -> Player2V2 -> Player2V1 -> Player1V1
Player1V1 = [230, 210, 4, 11,12, Player1,0]
Player1V2 = [350, 210, 4, 12,13, Player1,0]
Player1V3 = [470, 210, 4, 13,14, Player1,0]
Player1V4 = [590, 210, 4, 14,15, Player1,0]
Player1V5 = [710, 210, 4, 15,25, Player1,0]

Player2V5 = [710, 370, 4, 25,24, Player2,1]
Player2V4 = [590, 370, 4, 24,23, Player2,1]
Player2V3 = [470, 370, 4, 23,22, Player2,1]
Player2V2 = [350, 370, 4, 22,21, Player2,1]
Player2V1 = [230, 370, 4, 21,11, Player2,1]


def click(x, y):
    #move first
    x = 65536L * x / ctypes.windll.user32.GetSystemMetrics(0) + 1
    y = 65536L * y / ctypes.windll.user32.GetSystemMetrics(1) + 1
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVEABS, x, y, 0, 0)

    #then click
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_CLICK, 0, 0, 0, 0)

#Update the player score and display it...
#play = 0 means Player1 and play =1 means Player2
def update_player(disp,play=0,value=None):
    global Player1, Player2

    if play == 0:
        Player1 = Player1 + value
    else:
        Player2 = Player2 + value

    pygame.font.init()

 


    #initialize to display player score
    pygame.font.init()

    pygame.draw.rect(disp, OLIVE, (420, 110, 100, 40))
    pygame.draw.rect(disp, OLIVE, (420, 430, 100, 40))       
    
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font, 50)
    
    label_player1 = font_renderer.render(str(Player1), 50, RED)    
    disp.blit(label_player1 , (420, 110))
    pygame.display.update()

    label_player1 = font_renderer.render(str(Player1), 50, WHITE)    
    disp.blit(label_player1 , (420, 110))
    pygame.display.update()


    
    label_player2 = font_renderer.render(str(Player2), 50, RED)    
    disp.blit(label_player2, (420, 430))
    pygame.display.update()

    label_player2 = font_renderer.render(str(Player2), 50, WHITE)    
    disp.blit(label_player2, (420, 430))    
    pygame.display.update()



#find the next circle from the current circle....
# Player1V1 -> Player1V2 -> Player1V3 -> Player1V4 -> Player1V5 -> Player2V5
#  -> Player2V4 -> Player2V3 -> Player2V2 -> Player2V1 -> Player1V1    
def find_next(p):
    
    if Player1V1[3] == p[4]:
        return Player1V1
    elif Player1V2[3] == p[4]:
        return Player1V2
    elif Player1V3[3] == p[4]:
        return Player1V3
    elif Player1V4[3] == p[4]:
        return Player1V4
    elif Player1V5[3] == p[4]:
        return Player1V5
    elif Player2V1[3] == p[4]:
        return Player2V1
    elif Player2V2[3] == p[4]:
        return Player2V2
    elif Player2V3[3] == p[4]:
        return Player2V3
    elif Player2V4[3] == p[4]:
        return Player2V4
    elif Player2V5[3] == p[4]:
        return Player2V5

    
# Gui initialization for chanamane
def chanamane_gui(disp,p):  

    pygame.draw.circle(disp, OLIVE, (p[0], p[1]), 55)
    
  
    
#updates the number of pebbles in each circle and display it......
def update_pebbles(disp,p):

    pygame.font.init()
    chanamane_gui(disp,p)
    
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font, 50)
    
    label = font_renderer.render(str(p[2]), 50, RED)
    
    disp.blit(label, (p[0], p[1]))
    pygame.display.update()
    time.sleep(.1)

    label = font_renderer.render(str(p[2]), 50, WHITE)
    disp.blit(label, (p[0], p[1]))
    pygame.display.update()
    time.sleep(.1)

#updates the number of pebbles in each circle and display it......
def update_initial(disp,p):

    pygame.font.init()
    chanamane_gui(disp,p)
    
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font, 50)
    
    label = font_renderer.render(str(p[2]), 50, WHITE)
    
    disp.blit(label, (p[0], p[1]))
    pygame.display.update()
    time.sleep(.1)

#Update all pebbles and display it.
def update_all_pebbles(disp):
    update_pebbles(disp,Player1V1 )    
    update_pebbles(disp,Player1V2 )    
    update_pebbles(disp,Player1V3 )    
    update_pebbles(disp,Player1V4 )    
    update_pebbles(disp,Player1V5 )
    update_pebbles(disp,Player2V5 )    
    update_pebbles(disp,Player2V4 )    
    update_pebbles(disp,Player2V3 )    
    update_pebbles(disp,Player2V2 )    
    update_pebbles(disp,Player2V1 )

#Update initial pebbles and display it.
def update_initial_pebbles(disp):
    update_initial(disp,Player1V1 )    
    update_initial(disp,Player1V2 )    
    update_initial(disp,Player1V3 )    
    update_initial(disp,Player1V4 )    
    update_initial(disp,Player1V5 )
    update_initial(disp,Player2V5 )    
    update_initial(disp,Player2V4 )    
    update_initial(disp,Player2V3 )    
    update_initial(disp,Player2V2 )    
    update_initial(disp,Player2V1 )    
    
    
#RULES:
# 1. The first player picks up the seeds of one of his holes and distributes
#    them into the following holes one by one anti-clockwise.
# 2. After dropping the last seed into a hole, the contents of the following
#    hole are distributed in another lap.
# 3. The move ends when the following hole is empty. This is called "saada".
# 4. If the hole is empty, the player captures the contents of the succeeding hole.
#    "In addition, he captures the contents of the hole opposite to that hole."
# 5. Each turn a player may move twice, if he captures in his first move.
#    Then his term ends after two "saadas".
# 6. A player must move unless he has nothing to play with.
# 7. The game is finished when all counters are taken.
# 8. The player who has collected most counters wins the game.
# 10.In the next round, each player tries to fill his holes with five counters
#    from his winnings. These holes which cannot be filled are marked with a
#    pebble or a twig and are avoided for further play. The match is continued
#    until one player is unable to fill even one hole.    

def increment_pebbles(disp,p):

    exit_loop = False
    #print(p)
    last_circle = increment(disp, p)
    #print(last_circle)
    while last_circle[2] != 0:
        new_last_circle = find_next(last_circle)
        last_circle = increment(disp, new_last_circle)     
                         
        
    
    if last_circle[2] == 0 and exit_loop == False:
        #print(last_circle)
        current_circle = list(last_circle)
        next_circle = find_next(current_circle)
        #print(next_circle)
        
        if next_circle[2] != 0:
            update_player(disp,p[6],next_circle[2])
            next_circle[2] = 0
            update_pebbles(disp,next_circle)
            exit_loop = True




def increment(disp,p):
    
    current_circle = p
    current_pebble = p[2]
    current_circle[2] = 0
    update_pebbles(disp, current_circle)

    while current_pebble != 0:        
        next_circle = find_next(current_circle)               
        next_circle[2] = next_circle[2]+1
        current_pebble = current_pebble-1

        current_circle = list(next_circle)
        update_pebbles(disp, current_circle)

    return (current_circle)     
    
    
  
    
        
# Find out the user selected circle..... 
def user_choice(p):
    global Player
    if ((Player1V1[0]-55) <= p[0] <= (Player1V1[0]+55) and
         (Player1V1[1]-55) <= p[1] <= (Player1V1[1]+55)):
        Player =0
        return Player1V1
    elif ((Player1V2[0]-55) <= p[0] <= (Player1V2[0]+55) and
         (Player1V2[1]-55) <= p[1] <= (Player1V2[1]+55)):
        Player =0
        return Player1V2
    elif ((Player1V3[0]-55) <= p[0] <= (Player1V3[0]+55) and
         (Player1V3[1]-55) <= p[1] <= (Player1V3[1]+55)):
        Player =0
        return Player1V3
    elif ((Player1V4[0]-55) <= p[0] <= (Player1V4[0]+55) and
         (Player1V4[1]-55) <= p[1] <= (Player1V4[1]+55)):
        Player =0
        return Player1V4
    elif ((Player1V5[0]-55) <= p[0] <= (Player1V5[0]+55) and
         (Player1V5[1]-55) <= p[1] <= (Player1V5[1]+55)):
        Player =0
        return Player1V5        
    elif ((Player2V1[0]-55) <= p[0] <= (Player2V1[0]+55) and
         (Player2V1[1]-55) <= p[1] <= (Player2V1[1]+55)):
        Player =1
        return Player2V1
    elif ((Player2V2[0]-55) <= p[0] <= (Player2V2[0]+55) and
         (Player2V2[1]-55) <= p[1] <= (Player2V2[1]+55)):
        Player =1
        return Player2V2
    elif ((Player2V3[0]-55) <= p[0] <= (Player2V3[0]+55) and
         (Player2V3[1]-55) <= p[1] <= (Player2V3[1]+55)):
        Player =1
        return Player2V3
    elif ((Player2V4[0]-55) <= p[0] <= (Player2V4[0]+55) and
         (Player2V4[1]-55) <= p[1] <= (Player2V4[1]+55)):
        Player =1
        return Player2V4
    elif ((Player2V5[0]-55) <= p[0] <= (Player2V5[0]+55) and
         (Player2V5[1]-55) <= p[1] <= (Player2V5[1]+55)):
        Player =1
        return Player2V5        
    else:
         return None

#Sets the player whether it is computer or user based on the (x,y) co-ordinate clicked
def set_player(x,y):
    global Player
    if 100 <= x <= 850 and 100 <= y <= 300:
        Player = 0 #its computer playing
    elif 100 <= x <= 850 and 300 <= y <= 500:
        Player = 1 #Its User playing
    else:
        Player = None

def check_player(x,y):
    
    if 100 <= x <= 850 and 100 <= y <= 300:
        Player = 0 #its computer playing
    elif 100 <= x <= 850 and 300 <= y <= 500:
        Player = 1 #Its User playing
    else:
        Player = None
    return Player


def auto_click(disp):
    x = random.randint(100,850)
    y = random.randint(100,300)
    pygame.mouse.get_pressed()
    #win32api.SetCursorPos((x,y))
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    mouse_position = (x,y)
    current_player = user_choice(mouse_position)
    if current_player != None:
        if current_player[2] != 0:
            increment_pebbles(disp,current_player)

##
##def update_screen(user1, user2):
##    if user1 == True and user2 == False:

def get_userarea(pos):
    if 100 <= pos[0] <= 850 and 100 <= pos[1] <= 300:
        return 'area1'
    elif 100 <= pos[0] <= 850 and 300 <= pos[1] <= 500:
        return 'area2'
    
        
  
            


def main():
    global Player, User1, User2
    Player = 1
    pygame.init()
    
    
    
    DISPLAYSURF = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('Chennamane')
    DISPLAYSURF.fill(OLIVE)

    pygame.draw.rect(DISPLAYSURF, WHITE, (100, 100, 750, 400))
    pygame.draw.line(DISPLAYSURF, OLIVE, (100, 300), (850, 300), 5)
    
    pygame.draw.rect(DISPLAYSURF, OLIVE, (420, 110, 100, 40))
    pygame.draw.rect(DISPLAYSURF, OLIVE, (420, 430, 100, 40))

    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render( "Player", 10, OLIVE )
    DISPLAYSURF.blit(label, (100, 100))

    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render( "Computer", 10, OLIVE )
    DISPLAYSURF.blit(label, (100, 400)) 
    
    update_all_pebbles(DISPLAYSURF)    

    running = True  
    while running:
        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            if 100 <= mouse_position[0] <= 850 and 100 <= mouse_position[1] <= 300:
                if User1 == False:
                    pygame.mouse.set_visible(True)
                    mouse_click = pygame.mouse.get_pressed()
                    if mouse_click[0] == 1:
                        mouse_position = pygame.mouse.get_pos()
                        time.sleep(.2)
                        current_player = user_choice(mouse_position)
                        if current_player != None:
                            if current_player[2] != 0:
                                label = myfont.render( "Player", 15, RED )
                                DISPLAYSURF.blit(label, (100, 100))
                                label = myfont.render( "Computer",10, OLIVE )
                                DISPLAYSURF.blit(label, (100, 400))
                                increment_pebbles(DISPLAYSURF,current_player)
                                User1 = True
                                User2 = False

                        else:
                            update_player(DISPLAYSURF,current_player[6],0)


                            

                else:
                    print("To block")
                    pygame.event.set_blocked(pygame.KEYDOWN)
                    pygame.event.set_blocked(pygame.KEYUP)
                    xpos = random.randint(100,850)
                    ypos = random.randint(300,500)
                    pygame.mouse.set_pos(xpos, ypos)
                
                    
                    
                            
            
         
                
            elif 100 <= mouse_position[0] <= 850 and 300 <= mouse_position[1] <= 500:
                if User2 == False:
                    pygame.mouse.set_visible(False)
                    xpos = random.randint(100,850)
                    ypos = random.randint(300,500)
                    mouse_position = xpos, ypos
                    time.sleep(.2)
                    current_player = user_choice(mouse_position)
                    print(mouse_position)
##                    print(current_player)
                    if current_player != None:
                        if current_player[2] != 0:
                            label = myfont.render( "Player", 10, OLIVE )
                            DISPLAYSURF.blit(label, (100, 100))
                            label = myfont.render( "Computer",15, RED )
                            DISPLAYSURF.blit(label, (100, 400))
                            increment_pebbles(DISPLAYSURF,current_player)
                            User2 = True
                            User1 = False
                        else:
                            update_player(DISPLAYSURF,current_player[6],0)
                else:
                        print("To block")
                        pygame.event.set_blocked(pygame.KEYDOWN)
                        pygame.event.set_blocked(pygame.KEYUP)                    
                    

##                xpos = random.randint(100,850)
##                ypos = random.randint(100,300)
##                pygame.mouse.set_pos(xpos, ypos) 



            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        pygame.display.update()
    

    
if __name__ == '__main__':
    main()         
        
