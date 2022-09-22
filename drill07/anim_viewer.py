from pico2d import *
open_canvas()
character = load_image('sprite_animation1.png')
character_2 = load_image('sprite_animation2.png')
x = 0
y = 0
frame = 0
frame_1 = 0
while (x < 100):
    clear_canvas()
    character.clip_draw(frame * 100, 0, 90, 70, 400, 200)
    character_2.clip_draw(frame_1 * 100, 0, 90, 70, 400, 100)
    update_canvas()
    frame = (frame + 1) % 6
    frame_1 = (frame_1 + 1) % 6
    x+=1
    delay(0.08)
    get_events()

close_canvas()
