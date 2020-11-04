import pygame as pg
import  backgroundGrid as bg
pg.init()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLOCK_SIZE = (20,20)

screen = pg.display.set_mode((1280,720))


background = pg.Surface((screen.get_width(),screen.get_height()))
background.fill(pg.Color('#FFFFFF'))
backgroundGrid = bg.Grid(screen.get_width(),screen.get_height(),blockSize=BLOCK_SIZE)

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        screen.blit(background,(0,0))
        backgroundGrid.draw(screen)
        
        pg.display.update()
