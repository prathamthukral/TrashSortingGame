import pygame
import random
 
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0,0,255]
RED = [255,0,0]
GREEN = [0,255,0]
 
#height and width
SIZE = [800, 600]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Falling Animation")
clock = pygame.time.Clock()

data_list = []
pic_list = []
trash_list = []
difficulty = 4 #how many items are on the screen at once
dropYval = [1,1,1,1] #how fast the pieces fall, number of items of screen
droppedCount=0 #how many pieces of trash have fallen
recycleCount = 0 #how many recycle stuff has fallen
garbageCount = 0 #how many garbage stuff has fallen
height_list = []

ceilingList=[]
xvals = []
randx=0


def fontType(text,fg,bg,x,y,fontsize):
        font = pygame.font.Font(None, fontsize)
        size = font.size(text)
        ren = font.render(text, 0, fg, bg)
        screen.blit(ren, (x, y))

#menu screen
def menu():
        global done
        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                # Set the screen background
                screen.fill(WHITE)
                
                size=0
                font=0
                ren=0
                
                pygame.draw.rect(screen,[250,0,0],(int(SIZE[0]/2)-150,100,300,100))
                fontType('play',BLACK,RED,300,130,75)
                pygame.draw.rect(screen,[0,250,0],(int(SIZE[0]/2)-150,250,300,100))
                fontType('settings',BLACK,GREEN,300,270,75)
                pygame.draw.rect(screen,[0,0,250],(int(SIZE[0]/2)-150,400,300,100))
                fontType('quit',BLACK,BLUE,300,410,75)
                
                #hover
                if event.type==pygame.MOUSEMOTION:
                        mx,my=event.pos
                        if int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 100<=my<=200:
                                pygame.draw.rect(screen,[200,0,0],(int(SIZE[0]/2)-150,100,300,100))
                                fontType('play',BLACK,[200,0,0],300,130,75)
                        elif int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 250<=my<=350: 
                                pygame.draw.rect(screen,[0,200,0],(int(SIZE[0]/2)-150,250,300,100))
                                fontType('settings',BLACK,[0,200,0],300,270,75)
                        elif int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 400<=my<=500: 
                                pygame.draw.rect(screen,[0,0,200],(int(SIZE[0]/2)-150,400,300,100))
                                fontType('quit',BLACK,[0,0,200],300,410,75)
                if event.type==pygame.MOUSEBUTTONDOWN:
                        mx,my=event.pos
                        button=event.button
                        if int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 100<=my<=200 and button==1:
                                print("Game Loop initialize\n\n")
                                pygame.quit()
                                #quit()
                        elif int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 250<=my<=350 and button==1: 
                                settings()
                        elif int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 400<=my<=500 and button==1: 
                                pygame.draw.rect(screen,[0,0,200],(int(SIZE[0]/2)-150,400,300,100)) 
                                print("you quit\n\n")
                                pygame.quit()
                                #quit properly

                #/////////////////////////////////////////////////////////////////
                pygame.display.flip()
                clock.tick(60)
        pygame.quit()        
        pygame.draw.rect(screen,RED,(int(SIZE[0]/2)-150,100,300,100))
        pygame.draw.rect(screen,GREEN,(int(SIZE[0]/2)-150,250,300,100))
        pygame.draw.rect(screen,BLUE,(int(SIZE[0]/2)-150,400,300,100))
def settings():
        while True:
                screen.fill(WHITE)
                for event in pygame.event.get(pygame.KEYDOWN):
                                if event.key==pygame.K_ESCAPE:
                                        menu()
                #for event in pygame.event.get():
                 #       if event.type == pygame.QUIT:
                  #              pygame.quit()

                pygame.draw.rect(screen,BLUE,(100,100,100,80))
                fontType('esc',BLACK,BLUE,100,100,75)
                fontType('This is the settings page',BLACK,WHITE,350,200,40)
                fontType('press "esc" key to go back to main menu',BLACK,WHITE,250,250,40)
                pygame.display.flip()
#/////////////////////////////////////////////////////////////////////////
done = False
back=False
menu()
#while True:#game loop
        #x = input(": ")
        #if x =="yes": #if middle is clicked
                #while True: 
                        #back = input("back?: ")
                        #if back=='back':#if blue button is clicked
                                #break
        #elif x =="done":
                #break