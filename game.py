import pygame
pygame.init()
import os
import random
pygame.mixer.init()
#Defining Colors
white=(255,255,255)
red=(255,0,0)
magenta=(255,0,255)
blue=(0,0,255)
black=(0,0,0)
lime=(0,255,0)
screen_width=900
screen_height=600
gamewindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snakes")
pygame.display.update()
bgimg=pygame.image.load("snakes.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill(blue)
        text_screen("Welcome to Snakes!",red,260,250)
        text_screen("Press Space to Play Game!",red,232,290)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(60)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])
def game_loop():
    exit_game=False
    game_over=False
    snake_x=50
    snake_y=50
    snake_size=50
    velocity_x=0
    velocity_y=0
    food_x=random.randint(10,screen_width-10)
    food_y=random.randint(10,screen_height-10)
    score=0
    fps=30
    unit_velocity=5
    snake_length=1
    snake_list=[]

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore=f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            gamewindow.fill(white)
            text_screen("Game Over! Press Enter to Continue",red,135,275)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=unit_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-unit_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-unit_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=unit_velocity
                        velocity_x=0
            snake_x+=velocity_x
            snake_y+=velocity_y
            
            if(abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10):
                score+=10
                #print("Score is : ",score)
                food_x=random.randint(10,screen_width-10)
                food_y=random.randint(10,screen_height-10)
                snake_length+=5
                if(score>int(highscore)):
                    highscore=score

            gamewindow.fill(red)
            gamewindow.blit(bgimg,(0,0))
            text_screen("Score = "+str(score) +  "  Highscore = "+str(highscore),white,5,5)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if(len(snake_list)>snake_length):
                del snake_list[0]

            if(head in snake_list[:-1]):
                pygame.mixer.music.load('end.mp3')
                pygame.mixer.music.play()
                game_over=True
            if(snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height):
                pygame.mixer.music.load('end.mp3')
                pygame.mixer.music.play()
                game_over=True
                

            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            plot_snake(gamewindow,lime,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()