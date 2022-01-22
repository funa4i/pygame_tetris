import pygame

import pygame_widgets
from pygame_widgets.button import Button


def close_call():
    global run
    run = False


SIZE = width, height = 1366, 768
BUTTON_SIZE = btn_width, btn_height = 300, 150

pygame.init()
screen = pygame.display.set_mode(SIZE)



button_start = Button(
    screen,  # Surface to place button on
    width // 2 - (btn_width // 2),  # X-coordinate of top left corner
    height // 12,  # Y-coordinate of top left corner
    btn_width,  # Width
    btn_height,  # Height
    text='Начать игру',
    fontSize=50,
    margin=20,
    inactiveColour=(200, 50, 0),
    hoverColour=(150, 0, 0),
    pressedColour=(0, 200, 20),
    onClick=lambda: print('Click')
)

button_close = Button(
    screen,  # Surface to place button on
    width // 2 - (btn_width // 2),  # X-coordinate of top left corner
    (height // 12) * 2 + btn_height,  # Y-coordinate of top left corner
    300,  # Width
    150,  # Height
    text='Закрыть игру',
    fontSize=50,
    margin=20,
    inactiveColour=(200, 50, 0),
    hoverColour=(150, 0, 0),
    pressedColour=(0, 200, 20),
    onClick=lambda: close_call()
)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    screen.fill((255, 255, 255))

    pygame_widgets.update(events)
    pygame.display.update()
