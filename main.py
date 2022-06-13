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
    blocks = []
    blocks.append(Block(pos=[420, 69]))
    blocks.append(Block(pos=[9, 10]))
    blocks_to_drag = []  # probably initialise most of these variables in seperate file later on
    while running:
        display.fill(colour_black)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # breaks loop to quit
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # breaks loop and quits when esc pressed (useful for fullscreen)
                    running = False

            # Put actual code past here

            if event.type == pygame.MOUSEBUTTONDOWN:  # Use this for things that need a mouse up detection
                for block in blocks:
                    if block.rect.collidepoint(mouse_pos):  # need to implement layering, only top block can be dragged
                        block.dragging = True
                        blocks_to_drag.append(block)

            if event.type == pygame.MOUSEBUTTONUP:
                for block in blocks_to_drag:
                    block.dragging = False
                    block.drag_offset = None
                blocks_to_drag.clear()

        if pygame.mouse.get_pressed(num_buttons=3)[0]:  # Use this for things that only need to register a click
            pass

        for block in blocks_to_drag:
            block.drag(pos=mouse_pos)

        for block in blocks:
            block.render()

        # no code past here
        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    main()
