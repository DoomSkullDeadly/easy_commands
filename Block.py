import pygame
import itertools

size = 100, 60
s = pygame.Surface(size=size)
display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
counter = itertools.count()


class Block:
    def __init__(self, btype=None, pos=[0, 0]):
        self.id = next(counter)
        self.type = btype  # type of block, e.g. for loop, while loop, if, etc.
        self.clicked = False
        self.rect = pygame.Rect(pos, size)
        self.drag_offset = None
        self.highlight = False

    def render(self):
        pygame.draw.rect(surface=s, color=(100, 130, 60), rect=s.get_rect())  # idk how to not use s.get_rect() :/
        if self.highlight:
            pygame.draw.rect(surface=s, color=(150, 255, 90), rect=s.get_rect(), width=2)
        else:
            pygame.draw.rect(surface=s, color=(50, 100, 30), rect=s.get_rect(), width=2)  # outline
        display.blit(s, self.rect)

    def drag(self, pos=None):
        if not self.drag_offset:
            self.drag_offset = pos[0] - self.rect.x, pos[1] - self.rect.y
        if pos:
            self.rect.x = pos[0] - self.drag_offset[0]
            self.rect.y = pos[1] - self.drag_offset[1]
