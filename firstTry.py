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

clock = pg.time.Clock()

###Snake parameters###
snakeX = width/2
snakeXchange = 0

snakeY = height/2
snakeYchange = 0

snakeDiff = 10

tail = 0

newRoot = ""
newRoot = ""
###Snake parameters###

###Worm parameters###
wormX = 0
wormY = 0

def wormGenerator(X,Y):
    X = round(random.randrange(0,width,step = 10))
    Y = round(random.randrange(0,height,step = 10))
    return(X, Y)
###Worm parameters###

lastTail = 0
"""tailX = []
tailY = []"""

def tailGenerator(tail,snakeX,snakeY,lastTail,newRoot,lastRoot):
    tailLength = 0
    tailX = width/2
    tailY = height/2
    if tail >= 1:
        if tail > lastTail:
            if newRoot == "right":
                if lastRoot == "up":
                    i = 0
                    while tailLength <= tail:
                        
                        tailX = snakeX - 10
                        tailY = snakeY + 10 * tailLength
                        pg.draw.rect(frame,blue,[round(tailX),round(tailY),round(snakeDiff),round(snakeDiff)])
                        tailLength += 1
                        i += 1
                
            """if newRoot == "left":
                while tailLength < tail:
                    
                    tailX = snakeX + 10 * tailLength
                    tailY = snakeY
                    pg.draw.rect(frame,blue,[round(tailX),round(tailY),round(snakeDiff),round(snakeDiff)])
                    tailLength += 1

            if newRoot == "up":
                 while tailLength < tail:
                    
                    tailX = snakeX
                    tailY = snakeY - 10 * tailLength
                    pg.draw.rect(frame,blue,[round(tailX),round(tailY),round(snakeDiff),round(snakeDiff)])
                    tailLength += 1
            if newRoot == "down":
                while tailLength < tail:

                    tailX = snakeX
                    tailY = snakeY + 10 * tailLength
                    pg.draw.rect(frame,blue,[round(tailX),round(tailY),round(snakeDiff),round(snakeDiff)])
                    tailLength += 1"""

            lastTail = tail

    else:
        pass



wormX,wormY = wormGenerator(wormX,wormY)
print(wormX,wormY)

newRoot = ""
lastRoot = ""
while active:
    for event in pg.event.get():
        
        
        
        
        if event.type == pg.QUIT:
            active = False
            pg.quit()
            quit()
        

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                lastRoot = newRoot
                snakeXchange = -snakeDiff
                snakeYchange = 0
                newRoot = "left"
                print(newRoot)
            if event.key == pg.K_RIGHT:
                lastRoot = newRoot
                snakeXchange = snakeDiff
                snakeYchange = 0
                newRoot = "right"
                print(newRoot)
            if event.key == pg.K_DOWN:
                lastRoot = newRoot
                snakeYchange = snakeDiff
                snakeXchange = 0
                newRoot = "down"
                print(newRoot)
            if event.key == pg.K_UP:
                lastRoot = newRoot
                snakeYchange = -snakeDiff
                snakeXchange = 0
                newRoot = "up"
                print(newRoot)

    if snakeX >= width or  snakeX < 0 or  snakeY >= height or snakeY < 0 :
        active = False
        
    snakeX += snakeXchange
    snakeY += snakeYchange

    if snakeX == wormX and snakeY == wormY:
        wormX,wormY = wormGenerator(wormX,wormY)
        tail += 1
    


    frame.fill(white)
    pg.draw.rect(frame,black,[round(snakeX),round(snakeY),round(snakeDiff),round(snakeDiff)])
    
    tailGenerator(tail,snakeX,snakeY,lastTail,newRoot,lastRoot)

    pg.draw.rect(frame,red,[round(wormX),round(wormY),round(snakeDiff),round(snakeDiff)])
    pg.display.update()
    clock.tick(7)

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



