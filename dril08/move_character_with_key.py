from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 800, 600


def handle_events():
    global running
    global dir
    global dir_y
    global x, y, z

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                z = 1
                if x > KPU_WIDTH:
                    z = 3
                    x = KPU_WIDTH-80
            elif event.key == SDLK_LEFT:
                dir -= 1
                z = 0
                if x < 0:
                    z=2
                    x= 80
            elif event.key == SDLK_UP:
                dir_y += 1
                if y > KPU_HEIGHT:
                    y = KPU_HEIGHT - 70
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                if y < 0:
                    y = 40
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
z = 1
frame = 0
dir = 0
dir_y = 0
while running:
    clear_canvas()
    ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * z, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    y += dir_y * 5
    delay(0.01)

close_canvas()

