import pygame
import random
import math
from pygame import mixer

pygame.init()

FPS = 60
fpsclock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))

# background
background = pygame.image.load('background.png')

# you
ChungImg = []
ChungX = []
ChungY = []
ChungX_change = []
ChungY_change = []
num_of_chung = 5

for i in range(num_of_hai):
    ChungImg.append(pygame.image.load('chung.png'))
    ChungX.append(random.randint(0,735))
    ChungY.append(random.randint(20,150))
    ChungX_change.append(0.2)
    ChungY_change.append(20)

    def chung(x,y,i):
        screen.blit(chungImg[i],(x,y))

# your girl friend
TrangImg = pygame.image.load('trang.png')
TrangX = 380
TrangY = 500
TrangX_change = 0
TrangY_change = 0

def trang(x,y):
    screen.blit(trangImg,(x,y))

# heart
heartImg = pygame.image.load('heart.png')
heartX = 0
heartY = nganY
heartX_change = 0
heartY_change = 0.4

heart_state = "ready"

def heart(x,y):
    global heart_state
    heart_state = "fire"
    screen.blit(heartImg,(x+16,y+10))

# icon and title
title = pygame.display.set_caption("Anh Yêu Em")
icon = pygame.image.load('heart.png')
pygame.display.set_icon(icon)

# check colision
def iscollision(chungX,chungY,heartX,heartY):
    distance = math.sqrt(math.pow(chungX - heartX,2)+math.pow(chungY - heartY,2))

    if distance < 27:
        return True
    else:
        return False

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Yêu Anh x " + str(score_value),True, (150,150,255))
    screen.blit(score,(x,y))

# Game over
over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text = over_font.render("You lost but I still love u" ,True, (150,150,255))
    screen.blit(over_text,(30,250))

# sound and music
mixer.music.load("cauhon.wav")
mixer.music.play(-1)

running = True
while running:

    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                TrangX_change = 1
            if event.key == pygame.K_LEFT:
                TrangX_change = -1
            if event.key == pygame.K_UP:
                TrangY_change = -1
            if event.key == pygame.K_DOWN:
                TrangY_change = 1
            if event.key == pygame.K_SPACE:
                if heart_state == "ready":
                    heartX = trangX
                    heartY = trangY
                    heart(heartX,heartY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                TrangX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                TrangY_change = 0

    Trang(trangX,trangY)
    TrangX += trangX_change
    TrangY += trangY_change

    if trangX <=0:
        TrangX = 0 
    elif trangX >=736:
        TrangX = 736

    if trangY <= 400: 
        TrangY = 400
    elif trangY >=530:
        TrangY = 529

    for i in range(num_of_chung):
        # game over
        if chungY[i] > 200:
            for j in range(num_of_chung):
                ChungY[j] =2000
            game_over_text()
            break

        Chung(chungX[i],chungY[i],i)

        if chungX[i] <= 0:
            ChungX_change[i] = 0.2
            ChungY[i] += chungY_change[i]
        if chungX[i] >= 736:
            ChungX_change[i] = -0.2
            ChungY[i] += chungY_change[i]

        ChungX[i] += chungX_change[i]
           
        collision = iscollision(chungX[i],chungY[i],heartX,heartY)
        if collision:
            heart_state = "ready"
            ChungY[i] = random.randint(50,150)
            ChungX[i] = random.randint(0,735)
            score_value += 1
            explosion_sound = mixer.Sound('tick.wav')
            explosion_sound.play()

    if heartY <= 0:
        heartY = trangY
        heart_state ="ready" 
    if heart_state == "fire":
        heartY -= heartY_change
        heart(heartX,heartY)

    show_score(textX,textY)
    fpsclock.tick()
    pygame.display.flip()
