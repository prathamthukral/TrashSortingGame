#Pratham Thukral
#ICS3U1
#Sort-The-Trash

#importing applicable resources
import pygame
import random
 
#initializing pygame for graphics
pygame.init()

#colours
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0,0,255]
RED = [255,0,0]
GREEN = [0,255,0]
 
#height and width
SIZE = [800, 600]

#initiliazing screen display for game
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Falling Animation")
clock = pygame.time.Clock() #used to track frames per second/framerate

#Variables:
#used to track sources for images
pic_list = []
#used to track heights for images, matches up with pic_list
height_list = []
#a list used to track the random picture numbers, to decipher whether it was recycle or not
trash_list = []
#number of images on the screen at once
DIFFICULTY = 4
#defines how fast the image will fall down, or shift horizontally
dropYval = []
dropXval = []
#applies the initial values of 1 and 0 to the change in y and change in x
for x in range(DIFFICULTY):
    dropYval.append(1)
    dropXval.append(0)
#counts how many pieces hit the floor (the blue line)
droppedCount=0
#counter of successfully recycled items
recycleCount = 0
#counter of successfully garbaged items
garbageCount = 0
#2d list of x and y coordinates of a given image
coord_list = []
#counts number of milliseconds
milliseconds=0
#every 1000 ms, seconds has one added to it, used as a timer
seconds=0
#default colour of the character
CLOTHING=[0,153,255]
#initial gender of character, (can be changed from settings menu in game)
gender='M'
#Gets index value of image picked
whichClicked=-1

#When game is paused
def pauseScreen(mx,my):
    global done
    #basic validity checker
    screenIsPaused = True
    while screenIsPaused==True:
        #bg colour
        screen.fill(BLACK)
        #resume button
        pygame.draw.rect(screen,BLUE,(50,50,100,100))
        #text prompts
        fontType('Close window to quit game',WHITE,BLACK,100,270,50)
        fontType('Or click Blue Resume button',WHITE,BLACK,100,330,50)
        for event in pygame.event.get():
            #if the person closes window
            if event.type == pygame.QUIT:
                #fails both valid checks, one for pause screen, and one for game loop
                done = True
                screenIsPaused=False
                break
            #or if the person clicks the button
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mx,my=event.pos
                button=event.button
                #if the cursor is in the boundaries of the blue resume box
                if 50<=mx<=150 and 50<=my<=150 and button==1:
                    #fails validity check is failed
                    screenIsPaused=False
                    break
            pygame.display.flip()
    #returns the value of the gameloop validity check, if true, game should still run
    return done

#converts the random integer: pic, into a picture w/ its corresponding height
def numToPic(pic):
    #if the picture is some number: Set it to a specific image and corresponding height
    if pic==1:
        #tuple used to display images
        trashPic = ("imagesThukral/bottle.png",229)
    elif pic==2:
        trashPic= ("imagesThukral/box.png",100)
    elif pic==3:
        trashPic= ("imagesThukral/carton.png",145)
    elif pic==4:
        trashPic= ("imagesThukral/soda.png",174)
    elif pic==5:
        trashPic= ("imagesThukral/cup.png",100)
    elif pic==6:
        trashPic= ("imagesThukral/plate.png",100)
    elif pic==7:
        trashPic= ("imagesThukral/bag.png",123)
    elif pic==8:
        trashPic = ("imagesThukral/brush.png",208)
    #return the tuple that contains the information for that picture
    return trashPic

#initially defining the 4 images and their coordinates
def newPosInit():
    global DIFFICULTY,coord_list
    #used a counter variable - mimicks a for loop
    index=0
    #if the number is valid or not: 0 is the initial value
    failed=0
    #assigns DIFFICULTY number of integers to a list, w/o any overlaps
    while True:
        #randomly generated x and y coordinates
        xCoord = random.randint(50,650)
        yCoord = random.randint(-400,-300)
        #if the index is not in its first loop, validate the list before adding the new x and y coords
        if index!=0:
            #loops through every list item to see if it already exists
            for validator in range(len(coord_list)):
                #if the xCoord will overlap with another image
                if coord_list[validator][0]-103<xCoord<coord_list[validator][0]+103:
                    #another validator variable
                    breaker=False
                    #used at the end to see whether this image is valid, so it will be appended
                    failed=1
                    #while the xCoord is invalid
                    while breaker!=True:
                        #generates a new random number
                        xCoord=random.randint(50,650)
                        #if the new number is valid: break the loop
                        if xCoord<coord_list[validator][0]-103 or xCoord>coord_list[validator][0]+103:
                            #break the loop
                            breaker=True
                            failed=1
                            coord_list.append([xCoord,yCoord])
        #if all other numbers before this were valid, or if this is first number
        if x==0 or failed>-1:
            #automatically append
            coord_list.append([xCoord,yCoord])
        #counter index variable
        index+=1
        #if the index reaches the upperlimit, break the loop
        if index==DIFFICULTY+1:
            break
    #returns the 2dimensional list
    return coord_list

#creates the values as the old images reach the bottom of the screen
def newPos(index):
    #uses the index value from game loop to manipulate the values of x and y
    global DIFFICULTY, coord_list
    #for count in range(DIFFICULTY):
    xCoord = random.randint(50,650)
    #if the x coord is too close to another image, it will generate a new value
    if coord_list[index][0]-100<=xCoord<=coord_list[index][0]+100:
        while True:
            #generates new values till it is valid
            xCoord=random.randint(50,650)
            #if valid - break the loop
            if xCoord<coord_list[index][0]-100 or xCoord>coord_list[index][0]+100:
                break
    #return the single x value
    return xCoord

#draw garbage bags, use the parameter for number of bags needed
def pile(heightPile):
    #if there are more than or equal to 6 pieces of garbage, draw that many
    if heightPile<=6:
        #draw appropriate number of images
        for x in range(heightPile):
            screen.blit(pygame.image.load("imagesThukral/garbagebag.png"),(0,SIZE[1]-(x*100)))
    #draw appropriate number of images
    elif heightPile>6 and heightPile<=12:
        #draw appropriate number of images
        for x in range(7):
            screen.blit(pygame.image.load("imagesThukral/garbagebag.png"),(0,SIZE[1]-(x*100)))
        #draw appropriate number of images
        for x in range(heightPile-6):
            screen.blit(pygame.image.load("imagesThukral/garbagebag.png"),(100,SIZE[1]-(x*100)))
    #draw appropriate number of images
    elif heightPile==12:
        screen.blit(pygame.image.load("imagesThukral/garbagebag.png"),(100,100))
    #pygame.display.flip()

#shorthand for writing font with AA background
def fontType(text,fg,bg,x,y,fontsize):
    #set the font size
    font = pygame.font.Font(None, fontsize)
    size = font.size(text)
    #render the appropriate text in the right spot, use values from the parameters
    ren = font.render(text, 0, fg)
    #display
    screen.blit(ren, (x, y))

#draw the cursor character
def char(mx,my):
    global CLOTHING, gender
    #test the function:
    import math
    #head
    pygame.draw.circle(screen, CLOTHING, (mx,my-5),20)
    #body
    pygame.draw.rect(screen,CLOTHING,(mx-20,my+20,40,75))
    #right arm
    pygame.draw.line(screen,CLOTHING,(mx-20,my+20),(mx-40,my+55),10)
    pygame.draw.line(screen,CLOTHING,(mx-36,my+55),(mx-60,my+50),10)
    #left arm
    pygame.draw.line(screen,CLOTHING,(mx+20,my+20),(mx+30,my+50),10)
    pygame.draw.line(screen,CLOTHING,(mx+30,my+50),(mx-20,my+50),10)
    #right hand
    pygame.draw.circle(screen,CLOTHING,(mx-70,my+50),10)
    #trash can
    screen.blit(pygame.image.load("imagesThukral/trashcan.png"),(mx-75,my+15))
    #legs
    pygame.draw.line(screen,CLOTHING,(mx-5,my+55),(mx-20,my+170),15)
    pygame.draw.line(screen,CLOTHING,(mx+5,my+55),(mx+20,my+170),15)
    #shadow left arm
    pygame.draw.line(screen,[0,80,150],(mx+32,my+56),(mx-17,my+56),6)
    pygame.draw.line(screen,[0,80,150],(mx+25,my+45),(mx-17,my+45),1)
    #if character is male
    if gender.upper()=='M':
        #beard
        pygame.draw.arc(screen,[128,128,128],(mx-12,my-10,24,40),math.pi,1.5*math.pi,12)
        pygame.draw.arc(screen,[128,128,128],(mx-12,my-10,24,40),1.5*math.pi,2*math.pi,12)
        #shoes
        screen.blit(pygame.image.load("imagesThukral/menShoesLeft.png"),(mx-55,my+145))
        screen.blit(pygame.image.load("imagesThukral/menShoesRight.png"),(mx+9,my+145))
    #if character is female
    elif gender.upper()=='F':
        #draw hair
        #bg of head
        pygame.draw.rect(screen,RED,(mx-20,my-20,40,40))
        #redraw head
        pygame.draw.circle(screen, CLOTHING, (mx,my-5),20)
        #fg hair
        pygame.draw.arc(screen,RED,(mx-20,my-30,40,30),0,math.pi,15)
        #shoes
        screen.blit(pygame.image.load("imagesThukral/womenShoes.png"),(mx-50,my+130))

#shorthand to draw lines
def drawLine(color,x1,y1,x2,y2):
    #draw lines with all applicable parameters
    pygame.draw.line(screen,color,(x1,y1),(x2,y2),4)

#input the x and y values and return the index value
def getObjectByPoint(mx,my):
    global height_list
    #reset the index value so you can pick the right one at the end of this function
    resIndx = -1
    #loops through all index values to check whether the mouse is in the range of the image
    for index in range(DIFFICULTY):
        #x and y coordinates of the 'index' image
        xValue = coord_list[index][0]
        yValue = coord_list[index][1]
        #if the x value and the y value are valid: pass that index value
        if xValue<=mx<=xValue+100 and yValue<=my<=yValue+height_list[index]:
            resIndx = index
            return resIndx
    #if no value is valid, it passes -1
    return resIndx

#GAME LOOP
def gameLoop(event,gender):
    global droppedCount, recycleCount, garbageCount, DIFFICULTY, milliseconds, seconds, CLOTHING, whichClicked
    #runs the function to generate 4 pairs of x and y coordinates
    coords = newPosInit()
    #initial images, this is the first wave
    for randpick in range(DIFFICULTY):
        #get a random number to generate a picture
        pic = random.randint(1,8)
        #run the function that outputs the img source and height
        output = numToPic(pic)
        #image source gets appended
        pic_list.append(output[0])
        #heights get appended
        height_list.append(output[1])
        #appends the rand. number
        trash_list.append(pic)
    
    #number of mistakes made, takes away from total lives
    wrong=0
    #validator variable
    done = False
    #main loop
    while not done:
        # Set the screen background
        screen.fill(WHITE)
        #get all following events
        xCursor,yCursor=pygame.mouse.get_pos()
        for event in pygame.event.get():
            #if window is closed, quit game
            if event.type == pygame.QUIT:
                #exit value
                done = True
            #if mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #get x and y value of cursor
                mx,my = event.pos
                #get button value
                button = event.button
                #so you cant select multiple items
                if whichClicked==-1:
                    whichClicked=getObjectByPoint(mx,my)
                    if whichClicked != -1:
                        #if the image is clicked
                        if coord_list[whichClicked][0]<=mx<=coord_list[whichClicked][0]+100 and coord_list[whichClicked][1]<=my<=coord_list[whichClicked][1]+height_list[whichClicked] and button==1:
                            #it stops dropping
                            dropYval[whichClicked]=0
            #if a key is pressed
            if event.type == pygame.KEYDOWN:
                #if right arrow clicked
                if event.key==pygame.K_RIGHT and whichClicked!=-1:
                    #shift the image to right
                    dropXval[whichClicked]=15
                    #if it is garbage - player loses a life
                    if trash_list[whichClicked]>4:
                        wrong+=1
                        #danger image
                        screen.blit(pygame.image.load("imagesThukral/danger.png"),(0,0))
                        fontType('Lives left: '+str(5-wrong),BLACK,WHITE,300,270,75)
                        pygame.display.flip()
                        pygame.time.wait(500)
                    #if they direct it correctly
                    else:
                        recycleCount+=1
                    #reset the index value marker
                    whichClicked=-1
                #if they press left arrow instead
                elif event.key == pygame.K_LEFT and whichClicked!=-1:
                    #shift image to left
                    dropXval[whichClicked]=-15
                    #if the image is recycable
                    if trash_list[whichClicked]<5:
                        wrong+=1
                        screen.blit(pygame.image.load("imagesThukral/danger.png"),(0,0))
                        fontType('Lives left: '+str(5-wrong),BLACK,WHITE,300,270,75)
                        pygame.display.flip()
                        pygame.time.wait(500)
                    #if image is correctly sent to garbage
                    else:
                        garbageCount+=1
                    #reset index marker
                    whichClicked=-1
                #if escape key is clicked: pause the game w/ the pausefunction
                if event.key==pygame.K_ESCAPE:
                    done=pauseScreen(xCursor,yCursor)
        #draw lower boundary
        pygame.draw.line(screen,BLUE,(0,SIZE[1]-40),(SIZE[0],SIZE[1]-40),2)

        for i in range(DIFFICULTY):
            #output the picture with x and y coordinates
            coord_list[i][1] += dropYval[i]
            coord_list[i][0] += dropXval[i]
            #blit the image
            screen.blit(pygame.image.load(pic_list[i]),(coord_list[i][0],coord_list[i][1]))

            #If the image touches the bottom, or the sides, generate a new one above the screen
            if coord_list[i][1]+height_list[i] > SIZE[1]-40 or coord_list[i][0]<=-101 or coord_list[i][0]>=SIZE[0]:
                #only if the image touches the bottom, add one to dropped accumulator
                if coord_list[i][1]+height_list[i] > SIZE[1]-40:
                    droppedCount+=1
                #pick a new image
                pic = random.randint(1,8)
                trash_list[i] = pic
                #add the new image to the list
                output = numToPic(pic)
                pic_list[i] = output[0]
                #add corresponding height
                height_list[i] = output[1]
                
                #reset x dropper
                dropXval[i]=0
                #get new x and y coords
                coord_list[i][0] = newPos(i)
                coord_list[i][1] = random.randint(-400,-300)
                #progressing difficulty by changing y dropper
                if recycleCount+garbageCount<10 or droppedCount>3:
                    dropYval[i]=1
                elif 10<=recycleCount+garbageCount<20 or droppedCount>6:
                    dropYval[i]=2
                elif 20<=recycleCount+garbageCount<30 or droppedCount>8:
                    dropYval[i]=3
                elif 30<=recycleCount+garbageCount:
                    dropYval[i]=5
            if 1<droppedCount<13:
                pile(droppedCount)
                    #move the image
        #if too many items dropped or too many lives lost: GAME OVER
        if droppedCount==13 or wrong==5:
            done=True
        #timer, converts 1000 ms to 1 second
        if milliseconds > 1000:
            seconds += 1
            milliseconds -= 1000
        milliseconds += clock.tick_busy_loop(60)#loop every 1 second
        
        #time and lives
        fontType(str(seconds),BLACK,WHITE,SIZE[0]-85,100,50)
        fontType(str(5-wrong),BLACK,WHITE,SIZE[0]-85,150,50)
        
        #garbage bin
        pygame.draw.rect(screen,BLACK,(0,20,40,SIZE[1]-65))
        drawLine(WHITE,5,300,35,300)
        drawLine(WHITE,5,300,1,250)
        drawLine(WHITE,35,300,39,250)
        fontType('G',WHITE,WHITE,7,250,50)
        
        #recycle bin
        pygame.draw.rect(screen,BLUE,(SIZE[0]-40,20,40,SIZE[1]-65))
        screen.blit(pygame.image.load("imagesThukral/time.png"),(SIZE[0]-50,90))
        screen.blit(pygame.image.load("imagesThukral/lives.png"),(SIZE[0]-50,140))
        drawLine(WHITE,SIZE[0]-5,300,SIZE[0]-35,300)
        drawLine(WHITE,SIZE[0]-5,300,SIZE[0]-1,250)
        drawLine(WHITE,SIZE[0]-35,300,SIZE[0]-39,250)
        fontType('R',WHITE,WHITE,SIZE[0]-32,250,50)
        
        #character drawing
        char(xCursor,yCursor)
        
        pygame.display.flip()
        clock.tick(90)
    gameOver(droppedCount,garbageCount,recycleCount,wrong)
    
    #final output screen with scores
    print("Final outcomes:")
    print("Dropped:",droppedCount)
    print("Successfully Garbaged:",garbageCount)
    print("Successfully Recycled:",recycleCount)
    print("Lives lost",wrong,"\n\n")

#quitting from game:
def menu_quit():
    #x simulates a for loop, but dont know how long to run for
    x=0
    #while the circle doesnt fill screen
    while x<int(SIZE[0]/2)+100:
        #quit animation w/ black circle
        pygame.draw.circle(screen,BLACK,(int(SIZE[0]/2),int(SIZE[1]/2)),x)
        fontType('Goody Bye!',WHITE,RED,int(SIZE[0])/2-100,200,85)
        pygame.display.flip()
        x+=1
    pygame.quit()

#menu screen
def menu():
    global done, gender
    #while game is still running:
    while not done:
        #get pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #Set the screen background
            screen.fill(WHITE)
            
            #default settings used for fontType Function
            size=0
            font=0
            ren=0
            
            #menu buttons
            pygame.draw.rect(screen,[250,0,0],(int(SIZE[0]/2)-150,100,300,100))
            fontType('play',BLACK,RED,300,130,75)
            pygame.draw.rect(screen,[0,250,0],(int(SIZE[0]/2)-150,250,300,100))
            fontType('settings',BLACK,GREEN,300,270,75)
            pygame.draw.rect(screen,[0,0,250],(int(SIZE[0]/2)-150,400,300,100))
            fontType('quit',BLACK,BLUE,300,410,75)
            
            #hover
            if event.type==pygame.MOUSEMOTION:
                    mx,my=event.pos
                    #darken the corresponding button
                    if int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 100<=my<=200:
                            pygame.draw.rect(screen,[200,0,0],(int(SIZE[0]/2)-150,100,300,100))
                            fontType('play',BLACK,[200,0,0],300,130,75)
                    elif int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 250<=my<=350: 
                            pygame.draw.rect(screen,[0,200,0],(int(SIZE[0]/2)-150,250,300,100))
                            fontType('settings',BLACK,[0,200,0],300,270,75)
                    elif int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 400<=my<=500: 
                            pygame.draw.rect(screen,[0,0,200],(int(SIZE[0]/2)-150,400,300,100))
                            fontType('quit',BLACK,[0,0,200],300,410,75)
            #if button is clicked
            if event.type==pygame.MOUSEBUTTONDOWN:
                    mx,my=event.pos
                    button=event.button
                    #run gameLoop, settings, or menu_quit functions depending on button pressed
                    if int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 100<=my<=200 and button==1:
                            print("Game Loop initialize\n\n")
                            gameLoop(event,gender)
                    elif int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 250<=my<=350 and button==1: 
                            gender=settings()
                    elif int(SIZE[0]/2)-150<=mx<=int(SIZE[0]/2)+150 and 400<=my<=500 and button==1: 
                            pygame.draw.rect(screen,[0,0,200],(int(SIZE[0]/2)-150,400,300,100)) 
                            print("you quit\n")
                            menu_quit()
                            break
            pygame.display.flip()
            clock.tick(60)
    pygame.quit()

#settings screen
def settings():
        global gender
        while True:
            #bg colour
            screen.fill(WHITE)
            #get keyboard events
            for event in pygame.event.get(pygame.KEYDOWN):
                #if press escape, go back to main menu
                if event.key==pygame.K_ESCAPE:
                    menu()
                #if gender is changed, change gender value and font type
                if event.key==pygame.K_f:
                    gender='F'
                elif event.key==pygame.K_m:
                    gender='M'
            #text information
            fontType('Gender: '+gender,BLACK,WHITE,50,100,40)
            fontType('This is the settings page',BLACK,WHITE,50,200,40)
            #pause and back prompt
            fontType('"Esc" used to go back to main menu and pause game',BLACK,WHITE,50,250,40)
            #change gender prompt
            fontType('press "m" to change character to Male, or "f" to change to female',BLACK,WHITE,50,300,30)

            #instructions
            fontType('Instructions:',BLACK,WHITE,50,350,50)
            fontType('As trash falls from the sky, you must sort it!',BLACK,WHITE,50,400,30)
            fontType('Click on the trash and then direct it to the garbage bin or recycle bin',BLACK,WHITE,50,450,30)
            fontType('With arrow keys',BLACK,WHITE,50,500,30)
            fontType('Also, make sure your "pile" does not get too high!',BLACK,WHITE,50,550,30)
            pygame.display.flip()
        return gender

#if game is ended due to pile or lives lost
def gameOver(droppedCount,garbageCount,recycleCount,wrong):
    global screen,BLACK
    #black circle animation
    for x in range(800):
        pygame.draw.circle(screen,BLACK,(int(SIZE[0]/2),int(SIZE[1]/2)),x)
        pygame.display.flip()
    #game over and scores sheet
    fontType('You dropped: '+str(droppedCount),WHITE,WHITE,100,150,60)
    fontType('Successfully Garbaged: '+str(garbageCount),WHITE,WHITE,100,220,60)
    fontType('Successfully Recycled: '+str(recycleCount),WHITE,WHITE,100,290,60)
    fontType('Incorrect "Sorts": '+str(wrong),WHITE,WHITE,100,360,60)
    
    #loads back into the main menu to see if they want to play again
    fontType('Main Menu is Loading...',GREEN,GREEN,100,550,70)
    pygame.display.flip()
    pygame.time.wait(10000)
    menu()

#set at false so main game loop will run
done = False
#run the main menu function -> leads to all other functions
menu()
#final quit statement
pygame.quit()