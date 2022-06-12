import pygame

s = pygame.Surface(size=(100, 100))
display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)


class Block:
    def __init__(self, btype=None, pos=[0, 0]):
        self.type = btype  # type of block, e.g. for loop, while loop, if, etc.
        self.pos = pos
        self.clicked = False

    def render(self):
        pygame.draw.rect(surface=s, color=(100, 130, 60), rect=s.get_rect())
        display.blit(s, self.pos)

    def drag(self, change=[0, 0]):
        self.pos[0] += change[0]
        self.pos[1] += change[1]
