import pygame
import random
 
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0,0,255]
RED = [255,0,0]
GREEN = [0,255,0]
clothing = [0,153,255]
 
#height and width
SIZE = [800, 600]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Falling Animation")
clock = pygame.time.Clock()

#MAKE IT BUTTONS ON SCREEN RATHER THAN TYPE!///////////////////////////////////////////
#while True:
    #gender = input("Do you want male of female character? (type 'F' or 'M'): ")
    #gender = gender.upper()
    #if gender=='M' or gender=='MALE' or gender=='F' or gender=='FEMALE':
        #break
    #else:
        #print("\nSorry type in a valid input:")

        
def char(mx,my):
    #test the function:
    import math
    #head
    pygame.draw.circle(screen, clothing, (mx,my-5),20)
    #body
    pygame.draw.rect(screen,clothing,(mx-20,my+20,40,75))
    #right arm
    pygame.draw.line(screen,clothing,(mx-20,my+20),(mx-40,my+55),10)
    pygame.draw.line(screen,clothing,(mx-36,my+55),(mx-60,my+50),10)
    #left arm
    pygame.draw.line(screen,clothing,(mx+20,my+20),(mx+30,my+50),10)
    pygame.draw.line(screen,clothing,(mx+30,my+50),(mx-20,my+50),10)
    #right hand
    pygame.draw.circle(screen,clothing,(mx-70,my+50),10)
    #trash can
    screen.blit(pygame.image.load("Images/trashcan.png"),(mx-75,my+15))
    #legs
    pygame.draw.line(screen,clothing,(mx-5,my+55),(mx-20,my+170),15)
    pygame.draw.line(screen,clothing,(mx+5,my+55),(mx+20,my+170),15)
    #shadow left arm
    pygame.draw.line(screen,[0,80,150],(mx+32,my+56),(mx-17,my+56),6)
    pygame.draw.line(screen,[0,80,150],(mx+25,my+45),(mx-17,my+45),1)
    if gender.upper()=='M':
            #beard
            pygame.draw.arc(screen,[128,128,128],(mx-12,my-10,24,40),math.pi,1.5*math.pi,12)
            pygame.draw.arc(screen,[128,128,128],(mx-12,my-10,24,40),1.5*math.pi,2*math.pi,12)
            #shoes
            screen.blit(pygame.image.load("Images/menShoesLeft.png"),(mx-55,my+145))
            screen.blit(pygame.image.load("Images/menShoesRight.png"),(mx+9,my+145))
    elif gender.upper()=='F':
            #draw hair
            #bg of head
            pygame.draw.rect(screen,RED,(mx-20,my-20,40,40))
            #redraw head
            pygame.draw.circle(screen, clothing, (mx,my-5),20)
            #fg hair
            pygame.draw.arc(screen,RED,(mx-20,my-30,40,30),0,math.pi,15)
            #shoes
            screen.blit(pygame.image.load("Images/womenShoes.png"),(mx-50,my+130))



done = False
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    if event.type == pygame.MOUSEMOTION or event.type==pygame.MOUSEBUTTONUP:
        mx = event.pos[0]
        my = event.pos[1]
        screen.fill(WHITE)
        char(mx,my)
        

    pygame.display.flip()
    clock.tick(1200)
pygame.quit()
quit()