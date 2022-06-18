import pygame  # pygame 2.1.2
from Blocks import Blocks

pygame.init()

display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 18)

colour_white = (255, 255, 255)
colour_black = (0, 0, 0)
colour_green = (100, 130, 60)  # idk i randomly made it and thought it looked good for the "correct" colour

display.fill(colour_black)
pygame.display.update()


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, True, colour_white)
    return fps_text


def main():
    running = 1
    block_controller = Blocks()
    block_controller.new(pos=[420, 69])  # these are here just to test things
    block_controller.new(pos=[9, 10])

    while running:
        display.fill(colour_black)
        display.blit(update_fps(), (3, 3))  # fps counter for debug purposes
        mouse_pos = pygame.mouse.get_pos()  # Some code should go to start of main loop for logic in main loop
        block_controller.hover_over(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # breaks loop to quit
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # breaks loop and quits when esc pressed (useful for fullscreen)
                    running = False
                if event.key == pygame.K_SPACE:  # make new block at mouse position by pressing space
                    block_controller.new(pos=mouse_pos)

            # Put actual code past here

            if event.type == pygame.MOUSEBUTTONDOWN:  # Use this for things that need a mouse up detection
                block_controller.drag()

            if event.type == pygame.MOUSEBUTTONUP:
                block_controller.drop()

        if pygame.mouse.get_pressed(num_buttons=3)[0]:  # Use this for things that only need to register a click
            pass

        if block_controller.drag_this:
            block_controller.drag_this.drag(pos=mouse_pos)

        block_controller.render()

        # no code past here
        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    main()
