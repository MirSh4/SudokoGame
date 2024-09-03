import pygame as py
import os
from Grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d"%(400,100)

surface=  py.display.set_mode((1000,730))
py.display.set_caption("Sudoko")
py.font.init()
gameFont=py.font.SysFont('Comic Sans MS',50)
grid=Grid(gameFont)

steps=0



running=True

while running:
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
        if event.type == py.MOUSEBUTTONDOWN and not grid.win:
            if py.mouse.get_pressed()[0]:
                pos=py.mouse.get_pos()
                grid.get_mouse_click(pos[0],pos[1])
        if event.type == py.KEYDOWN:
            if grid.last_clicked is not None:
                steps+=1
                x, y = grid.last_clicked
                if event.unicode.isdigit():  # Check if the key is a digit
                    num = int(event.unicode)
                    grid.set_cell(x, y, num)  # Set the cell value
                    grid.last_clicked = None  # Reset the last clicked cell


    surface.fill((0,0,0))
    grid.draw_all(py,surface)
    if grid.win:
        steps_surface=gameFont.render(f"{steps} steps!",False,(0,255,0))
        won_surface=gameFont.render("You won!!",False,(0,255,0))
        surface.blit(won_surface,(750,400))
        surface.blit(steps_surface,(750,150))

    py.display.flip()






