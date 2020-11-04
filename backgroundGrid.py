import pygame as pg

class Grid(pg.sprite.Sprite):
    def __init__(self,window_width,window_height,fillColor = (22,160,133),outlineColor = (26,188,156),outlineThickness = 1,blockSize = (20,20)):
        self.width = window_width
        self.height = window_height
        self.fillCol = fillColor
        self.outlineColor = outlineColor
        self.sizeOfBlock = blockSize
        self.thickness = outlineThickness
    
    def make_grid(self):
        self.numberOfBlocks = (self.width * self.height) / (self.sizeOfBlock[0] * self.sizeOfBlock[1])
        self.listOfBlocks = []
        grid_x = 0
        grid_y = 0

        for i in range(0,self.width,self.sizeOfBlock[0]):
            for j in range(0,self.height,self.sizeOfBlock[1]):
                if i+self.sizeOfBlock[0] > self.width or j+self.sizeOfBlock[1] > self.height:
                    break
                tempBlock = pg.Rect(i,j,self.sizeOfBlock[0]-self.thickness,self.sizeOfBlock[1]-self.thickness)
                self.listOfBlocks.append(tempBlock)
            
    def draw(self,surface):
        self.make_grid()
        for block in self.listOfBlocks:
            pg.draw.rect(surface,self.outlineColor,(block[0],block[1],block[2]+self.thickness,block[3]+self.thickness),1)
            pg.draw.rect(surface,self.fillCol,block)



