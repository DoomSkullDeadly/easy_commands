import pygame  # pygame 2.0.0 used here
from Block import Block

pygame.init()

display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

clock = pygame.time.Clock()

colour_white = (255, 255, 255)
colour_black = (0, 0, 0)
colour_green = (100, 130, 60)  # idk i randomly made it and thought it looked good for the "correct" colour

display.fill(colour_black)
pygame.display.update()


def main():
    running = 1
    block = Block(pos=[420, 69])
    first_press = True
    while running:
        display.fill(colour_black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # breaks loop to quit
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # breaks loop and quits when esc pressed (useful for fullscreen)
                    running = False

        # put actual code here (make them functions/classes please, or it'll be one giant pain of a main func)
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if not first_press:
                dx, dy = mouse_pos[0] - old[0], mouse_pos[1] - old[1]
                block.drag(change=(dx, dy))
            first_press = False
            old = mouse_pos
        else:
            first_press = True

        block.render()

        # no code past here
        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    main()
