import pygame as pg
import  backgroundGrid as bg
import Snake
pg.init()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLOCK_SIZE = (20,20)

screen = pg.display.set_mode((1280,720))


background = pg.Surface((screen.get_width(),screen.get_height()))
background.fill(pg.Color('#FFFFFF'))
backgroundGrid = bg.Grid(screen.get_width(),screen.get_height(),blockSize=BLOCK_SIZE)
snakeBody = Snake.Snake(720,360,20,20)
snakeBody.create_snake()

run = True
clock = pg.time.Clock()

while run:
    events  = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
        snakeBody.get_keyboard_event(event)                          
    screen.blit(background,(0,0))
    backgroundGrid.draw(screen)
    snakeBody.draw(screen)
    snakeBody.move_snake()
    pg.display.update()
    clock.tick(30)

    
