import pygame as pg

moveAvailableAtCurrentTick = False

class Snake():
    def __init__(self,startPositionX,startPositionY,sizeX,sizeY,color = (52,152,219)):
        self.posX = startPositionX
        self.posY = startPositionY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.length = 1
        self.direction = 'left' #right,left,up,down
        self.snakeBlocks = []
        self.color = color

    def create_snake(self):
        self.head = pg.rect.Rect((self.posX,self.posY,self.sizeX,self.sizeY))


    def get_position(self):
        return (self.posX,self.posY)

    def draw(self,surface):
        pg.draw.rect(surface,self.color,self.head)

    def get_keyboard_event(self,event):
        global moveAvailableAtCurrentTick
        if event.type == pg.KEYDOWN:
            if not moveAvailableAtCurrentTick:
                return
            if event.key == pg.K_w and not self.direction == 'down':
                self.direction = 'up'
                print('up clicked')
            elif event.key == pg.K_a and not self.direction == 'right':
                self.direction = 'left'
                print('left clicked')
            elif event.key ==pg.K_d and not self.direction == 'left':
                self.direction = 'right'
                print('right clicked')
            elif event.key == pg.K_s and not self.direction == 'up':
                self.direction = 'down'
                print('down clicked')
            moveAvailableAtCurrentTick = False
    
    def move_snake(self):
        global moveAvailableAtCurrentTick
        if self.direction == 'right':
            self.head.move_ip(self.sizeX,0)
        elif self.direction == 'left':
            self.head.move_ip(-self.sizeX,0)
        elif self.direction =='up':
            self.head.move_ip(0,-self.sizeY)
        elif self.direction =='down':
            self.head.move_ip(0,self.sizeY)
        else:
            raise ValueError('WRONG DIRECTION',self.direction)

        moveAvailableAtCurrentTick = True
        



    