import pygame as pg
pg.init()


screen = pg.display.set_mode((1280,720))

background = pg.Surface((screen.get_width(),screen.get_height()))
background.fill(pg.Color('#FFFFFF'))
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        screen.blit(background,(0,0))
        pg.display.update()
