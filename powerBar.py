import pygame
pygame.init()
(6, 0)

SIZE_HEIGHT = 600
SIZE_WIDTH = 800

screen = pygame.display.set_mode((SIZE_WIDTH,SIZE_HEIGHT))
pygame.display.set_caption('Summative')
clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

#crashed = False
#chance=0
#count=0
#color=[255,50,255]

#def powerBar(chance,color):
    #pygame.draw.rect(screen,color,(100,100,110,chance))

##DOESNT WORK IN A FUNCTION
#def game():
    ##gameloop
    #global crashed, chance, count
    #while crashed!=True:
        #for event in pygame.event.get(): #gets any event that happens
            #if event.type == pygame.QUIT:
                #crashed=True
            
                    
        #pygame.draw.rect(screen,BLACK,(0,0,SIZE_WIDTH,SIZE_HEIGHT))
        #pygame.draw.rect(screen,RED,(100,100,110,200))
        
        ##1st half it increments slowly
        #if chance<100:
            #chance+=3
            #color[1]+=3
            #color[0]-=3
            #color[2]-=3        
        ##second half is faster    
        #else:
            #chance+=4
            #color[1]+=3
            #color[0]-=3
            #color[2]-=3         
        
        #if event.type ==pygame.KEYDOWN:
            #if event.key ==pygame.K_SPACE:
                #count+=1        
                #break
            
        
        #powerBar(chance,color)
        #if chance>202:
            #break
        
        #pygame.display.flip()
        #clock.tick(60)
    #pygame.quit()
    
    ##if they didn't press space at all (fail)
    #if count==0:
        #chance=0
    #print(str(int((chance/201)*100))+"%")
#game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
                
    screen.fill(BLACK)
    if event.type ==pygame.KEYDOWN:
        if event.key ==pygame.K_RIGHT:
            x = 0
            color=[255,50,255]
            pygame.draw.rect(screen,WHITE,(500,100,200,50))
            pygame.display.flip()

            counter = 0
            while counter!=151:
                if counter<100:
                    pygame.draw.rect(screen,color,(500,100,x,50))
                    x+=1
                else:
                    pygame.draw.rect(screen,color,(500,100,x,50))
                    x+=2                    
                if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        break                    
                pygame.display.flip()
                clock.tick(60)
                counter+=1
                if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        break
        elif event.key==pygame.K_LEFT:
            x = 0
            xPos = 300
            color=[255,50,255]
            pygame.draw.rect(screen,WHITE,(100,100,200,50))
            pygame.display.flip()

            counter = 0
            while counter!=151:
                if counter<100:
                    pygame.draw.rect(screen,color,(xPos,100,x,50))
                    x+=1
                    xPos-=1
                else:
                    pygame.draw.rect(screen,color,(xPos,100,x,50))
                    x+=2
                    xPos-=2
                if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        break                    
                pygame.display.flip()
                clock.tick(60)
                counter+=1
                if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        break        
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
quit()