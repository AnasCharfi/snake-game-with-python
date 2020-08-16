import pygame as pg
import time,random

pg.init()

width = 800
height = 600
frame = pg.display.set_mode((width,height))
pg.display.set_caption('Python game by Anas CHARFI')
active = True

blue = (0,0,255)
red = (255,0,0)
white = (255, 255, 255)
black = (0,0,0)

###Snake parameters###
snakeX = width/2
snakeXchange = 0

snakeY = height/2
snakeYchange = 0

snakeDiff = 10

tail = 1
###Snake parameters###

clock = pg.time.Clock()

wormX = 0
wormY = 0

def wormGenerator(X,Y):
    X = round(random.randrange(0,width+10,step = 10))
    Y = round(random.randrange(0,height+10,step = 10))
    return(X, Y)

lastTail = 0
def tailGenerator(tail,snakeX,snakeY,lastTail):
    tailLength = 0
    tailX = width/2
    tailY = height/2
    if tail >= 1:
        if tail > lastTail:
            tailX = snakeX - 10 
            tailY = snakeY
            
            while tailLength < tail:
                
                tailX = snakeX - 10 * tailLength
                tailY = snakeY
                pg.draw.rect(frame,blue,[round(tailX),round(tailY),round(snakeDiff),round(snakeDiff)])
                tailLength += 1
            lastTail = tail

    else:
        pass



wormX,wormY = wormGenerator(wormX,wormY)
print(wormX,wormY)

while active:
    for event in pg.event.get():
        
        
        
        
        if event.type == pg.QUIT:
            active = False
            pg.quit()
            quit()
        

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                snakeXchange = -snakeDiff
                snakeYchange = 0
            if event.key == pg.K_RIGHT:
                snakeXchange = snakeDiff
                snakeYchange = 0
            if event.key == pg.K_DOWN:
                snakeYchange = snakeDiff
                snakeXchange = 0
            if event.key == pg.K_UP:
                snakeYchange = -snakeDiff
                snakeXchange = 0

    if snakeX >= width or  snakeX < 0 or  snakeY >= height or snakeY < 0 :
        active = False
        
    snakeX += snakeXchange
    snakeY += snakeYchange

    if snakeX == wormX and snakeY == wormY:
        wormX,wormY = wormGenerator(wormX,wormY)
        tail += 1
    


    frame.fill(white)
    pg.draw.rect(frame,blue,[round(snakeX),round(snakeY),round(snakeDiff),round(snakeDiff)])
    
    tailGenerator(tail,snakeX,snakeY,lastTail)

    pg.draw.rect(frame,red,[round(wormX),round(wormY),round(snakeDiff),round(snakeDiff)])
    pg.display.update()
    clock.tick(20)

fontStyle = pg.font.SysFont(None,50)
msg = fontStyle.render("Game OVER",True,red)
frame.blit(msg, [round(width/2-100),round(height/2-25)])


signatureStyle = pg.font.SysFont(None,20)
signature = signatureStyle.render("Made with love by Anas CHARFI",True,black)
frame.blit(signature, [round(width-210),round(height-15)])
pg.display.update()
time.sleep(2)
pg.quit()
quit()



