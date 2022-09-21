from pico2d import *
import math
open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=400
y=90
z=0
i=0
while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x=x+2
    delay(0.001)
while(y<600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(770,y)
    y=y+2
    delay(0.001)
while(x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,580)
    x=x-2
    delay(0.001)
while(y>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(0,y)
    y=y-2
    delay(0.001)
    x=0
x=400
y=90
while(x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x+=math.cos(180/360*2*math.pi)
    y+=math.sin(180/360*2*math.pi)

    delay(0.001)
close_canvas()
