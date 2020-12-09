import pygame
import random
import time
import math
pygame.init()
pygame.mixer.init()
# dino position and calociyt
x=100
y=603
x_v=0
y_v=30
# bool variables
jump=False
stand=False
run=True
duck=False
bird=True
running=True

# game display
display=pygame.display.set_mode((1500,800))
pygame.display.set_caption("jumpLogic")
clock=pygame.time.Clock()


font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    display.blit(screen_text, [x,y])

# loading all image
img=pygame.image.load('cactus.png')
img=pygame.transform.scale(img,(100,150)).convert_alpha()
img2=pygame.image.load('cactus2.png')
img2=pygame.transform.scale(img2,(80,130)).convert_alpha()
K=[img,img,img,img,img]
K2=[img2,img2,img2,img2,img2]

runs=[pygame.image.load('update1.png'),
    pygame.image.load('update1.png'),
    pygame.image.load('update2.png'),
    pygame.image.load('update2.png')]

ducks=[pygame.image.load('duck1.png'),
    pygame.image.load('duck1.png'),
    pygame.image.load('duck2.png'),
    pygame.image.load('duck2.png')]

birds=[pygame.image.load('bird1.png'),
    pygame.image.load('bird1.png'),
    pygame.image.load('bird2.png'),
    pygame.image.load('bird2.png')]

stands=pygame.image.load('stand.png')
cactus_x=800
cactus_x2=800
bird_position=800
# speed n scroe
speed=30
scroe=0

# dino animatoins
birdIndex=0
animationIndex=0
duckIndex=0
def dino():
    
    global animationIndex
    display.fill((192,192,192))
    if animationIndex >3:
        animationIndex=0
    if run:
        display.blit(runs[animationIndex],(x,y))
        animationIndex+=1
    if stand:
        display.blit(stands,(x,y))
def duckAni():
    global duckIndex
    if duckIndex >3:
        duckIndex=0
    if duck:
        display.blit(ducks[duckIndex],(x,y+43))
        duckIndex+=1
# optilas animatoins    
def opticals():
    index=0
    if index>4:
        index=0
    if True:
        display.blit(K[index],(cactus_x,605))
        display.blit(K2[index],(cactus_x2,620))

def birdfly():
    
    global birdIndex
    if birdIndex>3:
        birdIndex=0
    if bird:
        display.blit(birds[birdIndex],(bird_position,600))
        pygame.draw.rect(display, ((255,0,0)),(bird_position+30,600+30,15,5), 5)
        birdIndex+=1

# mainloop
def calculateDistance(x1,y1,x2,y2):
    global dist
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(dist)
    return dist 

while running:
    dino()
    opticals() 
    duckAni()
    if scroe>1000:
        birdfly()
        if calculateDistance(x+100,y+100,bird_position+30,600+30)<30:
            scroe=0
            time.sleep(1)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            quit()
        UserInput=pygame.key.get_pressed()

        if UserInput[pygame.K_ESCAPE]:
            running=False
        if UserInput[pygame.K_UP]:
            jump=True
            stand=True 
            run=False 
            duck=False
        if UserInput[pygame.K_DOWN]:
            pygame.draw.rect(display, ((255,255,0)),(x+100,y+100+43,5,5), 5)
            run=False
            stand=False 
            duck=True
        if UserInput[pygame.K_SPACE]:
            jump=True
            stand=True 
            run=False 
            duck=False
        if UserInput[pygame.K_LEFT]:
            x-=10
        if UserInput[pygame.K_RIGHT]:
            x+=10
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                run=True
                duck=False
                stand=False

    if jump:
        y-=y_v*3 
        y_v-=4
        if y_v<-30:
            jump=False
            stand=False
            run=True
            y_v=30
    x+=x_v
    pygame.draw.line(display, ((255,255,255)), (0,750),(1500,750), 10)
    cactus_x-=speed
    cactus_x2-=speed
    bird_position-=speed
    text_screen(f"scroe{scroe}",(0,0,0),1100,15)
    scroe+=1
    if cactus_x<-30:
        cactus_x=1600
    if bird_position<-30:
        bird_position=2500
    if cactus_x2<-30:  
        cactus_x2=2000

    pygame.draw.rect(display, ((255,0,0)),(x+100,y+100,5,5), 5)
    pygame.draw.rect(display, ((0,255,0)),(cactus_x+70,635+30,5,5),5)
    pygame.draw.rect(display, ((0,255,0)),(cactus_x2+70,635+30,5,5),5)
    if calculateDistance(x+100,y+100,cactus_x+70,635+30)<50:
        scroe=0
        # time.sleep(1)
    if calculateDistance(x+100,y+100,cactus_x2+70,650+30)<50:
        scroe=0
        # time.sleep(1)

    clock.tick(25)   
    pygame.display.update()
       