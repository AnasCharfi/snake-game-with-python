import pygame as pg
import time
import random
 
pg.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
snakeColor = (85,107,47)
red = (190,0,0)
wormColor = (250,128,114)
background = (32,178,170)
 
frame_width = 600
frame_height = 400
 
frame = pg.display.set_mode((frame_width, frame_height))
pg.display.set_caption('Snake Game by Anas CHARFI')
#Icon Author: Freepik // www.flaticon.com
icon = pg.image.load("icon.png")
pg.display.set_icon(icon)
#frame.setIcon(icon)
 
clock = pg.time.Clock()
 
snake_step = 10
snake_speed = 15
 
 #SysFont("font type", size)
font_style = pg.font.SysFont("bahnschrift", 30)
font_score = pg.font.SysFont("comicsansms", 20)
font_signature = pg.font.SysFont("freesansbold",15,italic=True)
 
def snakeGenerator(snake_step, snake_list,Length_of_snake):
    for x in snake_list:
        # draw.rect( frame , color,[positionX, positionY,height,width])

        pg.draw.rect(frame, snakeColor, [round(x[0]), round(x[1]), snake_step, snake_step])
        score(Length_of_snake)
        
 
def score(Length_of_snake):
    msg = "Score " + str(Length_of_snake)
    mes = font_score.render(msg, True, yellow)
    frame.blit(mes, [0 + mes.get_width() //2 , 0 + mes.get_height() // 2])

def message(msg, color):
    mes = font_style.render(msg, True, color)
    frame.blit(mes, [300 - mes.get_width() //2 , 200 - mes.get_height() // 2])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = frame_width / 2
    y1 = frame_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, frame_width - snake_step) / 10.0) * 10.0
    foody = round(random.randrange(0, frame_height - snake_step) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            frame.fill(background)
            message("You Lost! Press C-Play Again or Q-Quit", red)

            signature = "Game made with love by Anas CHARFI"
            mes = font_signature.render(signature, True, black)
            frame.blit(mes, [600 - mes.get_width()  , 400 - mes.get_height() ])
 
            pg.display.update()
 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_c:
                        gameLoop()
            
 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake_step
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = snake_step
                    y1_change = 0
                elif event.key == pg.K_UP:
                    y1_change = -snake_step
                    x1_change = 0
                elif event.key == pg.K_DOWN:
                    y1_change = snake_step
                    x1_change = 0
 
        if x1 >= frame_width or x1 < 0 or y1 >= frame_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        frame.fill(background)
        pg.draw.rect(frame, wormColor, [round(foodx), round(foody), snake_step, snake_step])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        snakeGenerator(snake_step, snake_List,Length_of_snake)
 
 
        pg.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, frame_width - snake_step) / 10.0) * 10.0
            foody = round(random.randrange(0, frame_height - snake_step) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pg.quit()
    quit()
 
 
gameLoop()
